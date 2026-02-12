import os
import glob
from PIL import Image, ImageDraw


def find_best_source_image(directory):
    # Potential source directories
    search_paths = [
        os.path.join(directory, "images"),
        os.path.join(directory, "images", "app_icon"),
        directory  # Root of the app dir
    ]

    candidates = []
    for path in search_paths:
        if os.path.exists(path):
            candidates.extend(glob.glob(os.path.join(path, "*.png")))

    if not candidates:
        return None

    # Heuristics:
    # 1. Prefer files with "app_icon" or "1024" in name
    # 2. Sort by size (larger is better)

    def score_candidate(path):
        score = 0
        filename = os.path.basename(path).lower()
        if "app_icon" in filename:
            score += 10
        if "1024" in filename:
            score += 5
        if "logo" in filename:
            score += 2

        # Filesize tie-breaker (max 5 points for size)
        try:
            size = os.path.getsize(path)
            score += min(size / 1_000_000, 5)
        except:
            pass

        return score

    candidates.sort(key=score_candidate, reverse=True)
    return candidates[0]


def create_circular_icon(source_path, output_path):
    """
    High-quality circular icon generation using supersampling and Lanczos resampling.
    """
    try:
        # 1. Open source and convert to RGBA
        img = Image.open(source_path).convert("RGBA")
        
        # 2. Crop to square (center)
        w, h = img.size
        size = min(w, h)
        if w != h:
            left = (w - size) // 2
            top = (h - size) // 2
            img = img.crop((left, top, left + size, top + size))
        
        # 3. Create a high-resolution canvas (SUPERSAMPLING)
        # We'll work at 4x the resolution of the largest target icon size (256px)
        # or the original image size, whichever is appropriate.
        # Let's fix the working resolution to a high value like 1024x1024
        # to ensure consistent quality for the 256px icon.
        work_size = 1024
        
        # Resize source to work_size using Lanczos
        img_high_res = img.resize((work_size, work_size), resample=Image.Resampling.LANCZOS)
        
        # 4. Create a high-res circular mask
        # Initialize with '0' (transparent/black)
        mask = Image.new("L", (work_size, work_size), 0)
        draw = ImageDraw.Draw(mask)
        
        # Draw white circle.
        # Leave a tiny padding (1px at 1024px ~ 0.1%) to ensure anti-aliasing doesn't get cut off
        padding = 0 
        draw.ellipse((padding, padding, work_size - 1 - padding, work_size - 1 - padding), fill=255)
        
        # 5. Apply mask to image
        # Initialize base with TRANSPARENT WHITE (255, 255, 255, 0) to prevent black halos on edges
        result_high_res = Image.new("RGBA", (work_size, work_size), (255, 255, 255, 0))
        result_high_res.paste(img_high_res, (0, 0), mask=mask)
        
        # 6. Generate multiple sizes using Lanczos resampling
        # Target sizes for ICO
        target_sizes = [256, 64, 48, 32, 16]
        icon_images = []
        
        for s in target_sizes:
            # Resize the high-quality masked image down to target size
            resized_icon = result_high_res.resize((s, s), resample=Image.Resampling.LANCZOS)
            icon_images.append(resized_icon)
            
        # 7. Save as ICO
        # The first image is the base, others are appended.
        # It's good practice to have the largest one first or last.
        # Pillow's ICO plugin handles this list.
        # We'll use the 256px version as the primary save target and append the others.
        
        base_icon = icon_images[0]
        other_icons = icon_images[1:]
        
        base_icon.save(output_path, format="ICO", append_images=other_icons)
        print(f"  Success! Generated {output_path} (Sizes: {target_sizes})")
        return True
        
    except Exception as e:
        print(f"  Error processing {source_path}: {e}")
        return False


def generate_circular_favicon_for_dir(app_dir):
    print(f"Processing {app_dir}...")
    source_image = find_best_source_image(app_dir)

    if not source_image:
        print(f"  No suitable PNG found in {app_dir}. Skipping.")
        return

    print(f"  Found source: {source_image}")
    output_ico = os.path.join(app_dir, "favicon.ico")
    create_circular_icon(source_image, output_ico)


def main():
    # List of directories to process
    target_directories = [
        "LearningStatistics",
        "SharedDice",
        "FunTopics",
        "KanjiAwaAwaPon",
        "TimesTablesMemoryAwaAwaPon",
        "TapAlbum",
        "NumberPlaceHint",
        "AwaAwaPon",
        "MyDreams100",
        "PostDrafts",
        "FlagMemoryAwaAwaPon",
        "GoodLuckMaker"
    ]

    # Process root favicon as well
    root_dir = "."
    root_source = os.path.join("commonImages", "fabicons", "20250614_100210.png")
    
    if os.path.exists(root_source):
        print("Processing root favicon...")
        print(f"  Found source: {root_source}")
        output_ico = os.path.join(root_dir, "favicon.ico")
        create_circular_icon(root_source, output_ico)
    else:
        print(f"Root source image not found: {root_source}")

    for relative_dir in target_directories:
        # Construct full path or verify it exists relative to cwd
        if os.path.isdir(relative_dir):
            generate_circular_favicon_for_dir(relative_dir)
        else:
            print(f"Directory not found: {relative_dir}")


if __name__ == "__main__":
    main()
