import os
import subprocess
import glob

def find_best_source_image(directory):
    # Potential source directories
    search_paths = [
        os.path.join(directory, "images"),
        os.path.join(directory, "images", "app_icon"),
        directory # Root of the app dir
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

def generate_circular_favicon_for_dir(app_dir):
    print(f"Processing {app_dir}...")
    source_image = find_best_source_image(app_dir)
    
    if not source_image:
        print(f"  No suitable PNG found in {app_dir}. Skipping.")
        return

    print(f"  Found source: {source_image}")
    
    # Temporary intermediate file
    output_png = os.path.join(app_dir, "temp_circular_favicon.png")
    output_ico = os.path.join(app_dir, "favicon.ico")

    # 1. Generate circular PNG
    # Use geq filter to create a circular alpha mask
    command_png = [
        "ffmpeg", "-y",
        "-i", source_image,
        "-filter_complex",
        "[0:v]format=rgba[base];"
        "[base]split[img][img2];"
        "[img2]format=gray,geq='if(lte(pow(X-(W/2),2)+pow(Y-(H/2),2),pow(min(W/2,H/2)-2,2)),255,0)'[mask];"
        "[img][mask]alphamerge",
        output_png
    ]
    
    try:
        subprocess.run(command_png, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"  Error generating PNG: {e.stderr.decode()}")
        return

    # 2. Generate ICO from circular PNG
    # Resize to 32x32 for favicon.ico
    command_ico = [
        "ffmpeg", "-y",
        "-i", output_png,
        "-vf", "scale=32:-1",
        output_ico
    ]
    
    try:
        subprocess.run(command_ico, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"  Success! Generated {output_ico}")
    except subprocess.CalledProcessError as e:
        print(f"  Error generating ICO: {e.stderr.decode()}")
    finally:
        # Cleanup temp file
        if os.path.exists(output_png):
            os.remove(output_png)

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
    
    # Process root favicon as well (original logic, basically)
    # But for now, let's focus on the update request which was about subfolders.
    # The user asked: "originally did this for root, now do for others".
    
    for relative_dir in target_directories:
        # Construct full path or verify it exists relative to cwd
        if os.path.isdir(relative_dir):
            generate_circular_favicon_for_dir(relative_dir)
        else:
            print(f"Directory not found: {relative_dir}")

if __name__ == "__main__":
    main()
