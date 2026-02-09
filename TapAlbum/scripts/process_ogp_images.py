import os
import subprocess
import glob

def process_ogp_images():
    # Base directory relative to project root
    base_dir = "TapAlbum/images/ogp_images"
    
    # Target dimensions
    target_width = 1200
    target_height = 630
    
    # Find all png files in language subdirectories
    # Pattern: TapAlbum/images/ogp_images/<lang>/*.png
    # We want to process the *first* png found in each lang dir that is NOT already the output file
    
    languages = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for lang in languages:
        lang_dir = os.path.join(base_dir, lang)
        png_files = glob.glob(os.path.join(lang_dir, "*.png"))
        
        # Filter out the output file if it already exists to avoid re-processing it as input
        input_files = [f for f in png_files if "ogp_image.png" not in f]
        
        if not input_files:
            print(f"Skipping {lang}: No input PNG found.")
            continue
            
        # Take the first available PNG as input
        input_file = input_files[0]
        output_file = os.path.join(lang_dir, "ogp_image.png")
        
        print(f"Processing {lang}: {input_file} -> {output_file}")
        
        # ffmpeg command to resize and pad
        # scale=1200:630:force_original_aspect_ratio=decrease : Fit inside 1200x630
        # pad=1200:630:(ow-iw)/2:(oh-ih)/2:white : Pad to 1200x630 with white background, centered
        
        command = [
            "ffmpeg", "-y",
            "-i", input_file,
            "-vf", f"scale={target_width}:{target_height}:force_original_aspect_ratio=decrease,pad={target_width}:{target_height}:(ow-iw)/2:(oh-ih)/2:white",
            output_file
        ]
        
        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"  Successfully created {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"  Error processing {lang}: {e.stderr.decode()}")

if __name__ == "__main__":
    process_ogp_images()
