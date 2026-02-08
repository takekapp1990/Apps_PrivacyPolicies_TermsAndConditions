import os
import subprocess

def generate_gifs():
    # Base directory relative to where the script is run (project root)
    base_dir = "TapAlbum/images/screen_shots"
    
    # Common files to be placed at the end in specific order
    common_files_ordered = [
        "Simulator Screenshot - iPhone 16 Pro Max - 2026-02-08 at 10.12.05.png",
        "Simulator Screenshot - iPhone 16 Pro Max - 2026-02-08 at 10.11.33.png"
    ]

    # Check if base directory exists
    if not os.path.exists(base_dir):
        print(f"Error: Directory '{base_dir}' not found. Make sure you are running this script from the project root.")
        return

    # Iterate through each language directory
    for lang_dir in sorted(os.listdir(base_dir)):
        lang_path = os.path.join(base_dir, lang_dir)
        
        if not os.path.isdir(lang_path):
            continue

        print(f"Processing directory: {lang_path}")

        all_files = [f for f in os.listdir(lang_path) if f.endswith(".png") and not f.startswith("._")]
        
        main_files = []
        found_common_files_set = set()

        # Separate main files and common files
        for f in all_files:
            if f in common_files_ordered:
                found_common_files_set.add(f)
            else:
                main_files.append(f)
        
        # Sort main files by filename (timestamp)
        main_files.sort()

        # Construct the final list of full paths
        final_file_paths = []
        
        # Add main files first
        for f in main_files:
             final_file_paths.append(os.path.join(lang_path, f))

        # Append common files in the specified order if they exist in this directory
        for common_file in common_files_ordered:
            if common_file in found_common_files_set:
                final_file_paths.append(os.path.join(lang_path, common_file))
            else:
                print(f"  Warning: Common file '{common_file}' not found in {lang_dir}")

        if not final_file_paths:
            print(f"  No suitable PNG files found in {lang_dir}, skipping.")
            continue

        # Create a temporary file list for ffmpeg
        list_file_path = os.path.join(lang_path, "file_list.txt")
        try:
            with open(list_file_path, "w") as f:
                for i, file_path in enumerate(final_file_paths):
                    abs_path = os.path.abspath(file_path)
                    f.write(f"file '{abs_path}'\n")
                    
                    # Check if it is the last file
                    if i == len(final_file_paths) - 1:
                        f.write("duration 1.8\n") # Last frame shorter (1.0s)
                    else:
                        f.write("duration 2.25\n") # 1.5x of original 1.5s = 2.25s
                
                # Repeat the last file to ensure the last frame is shown for its duration
                if final_file_paths:
                    abs_path = os.path.abspath(final_file_paths[-1])
                    f.write(f"file '{abs_path}'\n")

            output_gif = os.path.join(lang_path, "animated_screenshot.gif")
            
            # FFmpeg command
            # We use a filter complex for better GIF quality (palettegen).
            # splitting the stream, generating palette from one, applying to other.
            filter_complex = "fps=10,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"
            
            cmd = [
                "ffmpeg",
                "-y", # Overwrite output
                "-f", "concat",
                "-safe", "0",
                "-i", list_file_path,
                "-vf", filter_complex,
                "-loop", "0",
                output_gif
            ]

            # Run ffmpeg
            # print(f"  Running ffmpeg...")
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"  Successfully created {output_gif}")

        except subprocess.CalledProcessError as e:
            print(f"  Error creating GIF for {lang_dir}: {e}")
        except Exception as e:
             print(f"  An unexpected error occurred: {e}")
        finally:
            if os.path.exists(list_file_path):
                os.remove(list_file_path)

if __name__ == "__main__":
    generate_gifs()
