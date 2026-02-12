import os
import subprocess
import shutil

def generate_gifs():
    # Base directory relative to where the script is run (project root)
    base_dir = "TapAlbum/images/screen_shots"
    
    # File to exclude
    exclude_file = "Simulator Screenshot - iPhone 16 Pro Max - 2026-02-08 at 10.12.05.png"
    
    # File to place at 4th position (index 3)
    target_file = "Simulator Screenshot - iPhone 16 Pro Max - 2026-02-08 at 10.11.33.png"
    
    # Video file path
    video_file = os.path.join(base_dir, "TapAlbumScshoMovie.mp4")

    # Check existence
    if not os.path.exists(base_dir):
        print(f"Error: Directory '{base_dir}' not found.")
        return

    if not os.path.exists(video_file):
        print(f"Error: Video file '{video_file}' not found.")
        return

    # Iterate through each language directory
    for lang_dir in sorted(os.listdir(base_dir)):
        lang_path = os.path.join(base_dir, lang_dir)
        
        if not os.path.isdir(lang_path):
            continue

        print(f"Processing directory: {lang_path}")

        # === Step 1: Generate temp_screenshots.gif ===
        all_files = [f for f in os.listdir(lang_path) if f.endswith(".png") and not f.startswith("._")]
        filtered_files = []
        target_file_found = False

        for f in all_files:
            if f == exclude_file:
                continue
            if f == target_file:
                target_file_found = True
                continue
            filtered_files.append(f)
        
        filtered_files.sort()
        
        if target_file_found:
            insert_index = 3
            if insert_index > len(filtered_files):
                insert_index = len(filtered_files)
            filtered_files.insert(insert_index, target_file)
        
        if not filtered_files:
            print(f"  No suitable PNG files found, skipping.")
            continue

        final_file_paths = [os.path.join(lang_path, f) for f in filtered_files]
        
        temp_screenshots_gif = os.path.join(lang_path, "temp_screenshots.gif")
        list_file_path = os.path.join(lang_path, "file_list_screenshots.txt")

        # Create list file for screenshots
        with open(list_file_path, "w") as f:
            for i, file_path in enumerate(final_file_paths):
                abs_path = os.path.abspath(file_path)
                f.write(f"file '{abs_path}'\n")
                
                # Check if it is the last file
                if i == len(final_file_paths) - 1:
                    f.write("duration 1.0\n") # Last frame shorter
                else:
                    f.write("duration 2.25\n")

            # Repeat last frame
            if final_file_paths:
                f.write(f"file '{os.path.abspath(final_file_paths[-1])}'\n")

        # Generate screenshots GIF with resizing
        # Using palettegen for better quality
        print("  Generating screenshots GIF...")
        filter_complex = "fps=10,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", list_file_path,
            "-vf", filter_complex,
            temp_screenshots_gif
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        os.remove(list_file_path)

        # === Step 2: Generate temp_video.gif ===
        temp_video_gif = os.path.join(lang_path, "temp_video.gif")
        print("  Generating video GIF from MP4...")
        
        # Convert MP4 to GIF (resizing to 600 width, 10fps to match)
        filter_complex_video = "fps=10,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"
        subprocess.run([
            "ffmpeg", "-y",
            "-i", video_file,
            "-vf", filter_complex_video,
            "-loop", "0", # Loop 0 (infinite) usually logic for GIFs, but here strictly intermediate
            temp_video_gif
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        # === Step 3: Concatenate GIFs ===
        final_output = os.path.join(lang_path, "animated_screenshot.gif")
        print("  Concatenating GIFs...")
        
        # Concatenate two GIFs
        # We use concat filter.
        # Note: concat filter requires same dimensions. Both are scaled to width 600.
        # Height might vary if aspect ratios differ. We might need to force scale/pad? 
        # Assuming typical screenshot aspect ratio matches video aspect ratio for now.
        # If concatenation fails due to resolution, we may need complex filterpad.
        
        # We will use simple concat demuxer on GIFs if possible? No, GIF concat is tricky with palettes.
        # Better to use filter_complex concat.
        
        # The filter: [0:v][1:v]concat=n=2:v=1:a=0[outv]
        # We also need to ensure compatible pixel formats.
        
        try:
            subprocess.run([
                "ffmpeg", "-y",
                "-i", temp_screenshots_gif,
                "-i", temp_video_gif,
                "-filter_complex", "[0:v][1:v]concat=n=2:v=1[outv]",
                "-map", "[outv]",
                "-loop", "0", # Final GIF loops
                final_output
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"  Successfully created {final_output}")
            
        except subprocess.CalledProcessError as e:
            print(f"  Error concatenating: {e}")
            # Fallback: if resolution mismatch (height), maybe force scale video to match screenshots height?
            # But earlier strict resize to width 600 should handle it if aspect ratio is same.
            
        # Clean up
        if os.path.exists(temp_screenshots_gif):
            os.remove(temp_screenshots_gif)
        if os.path.exists(temp_video_gif):
            os.remove(temp_video_gif)

if __name__ == "__main__":
    generate_gifs()
