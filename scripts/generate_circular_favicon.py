import os
import subprocess

def generate_circular_favicon():
    # Paths (relative to project root)
    input_image = "commonImages/fabicons/20250614_100210.png"
    output_ico = "favicon.ico"
    output_png = "commonImages/fabicons/favicon_circle.png"
    
    # 1. Generate circular PNG
    # Use geq filter to create a circular alpha mask
    # Corrected filter syntax for geq: separate plane expressions with ':'
    # p(0) is alpha plane (not supported directly in geq for RGBA input usually without extraction using alphaextract)
    # Alternative approach: create a mask separately and combine
    
    # Approach:
    # 1. Create a circular mask (white circle on black background)
    # 2. Apply this mask to the alpha channel of the input image
    
    # Simplified filter_complex:
    # [0:v]format=rgba,split[base][mask];
    # [mask]geq=r='if(lte(pow(X-(W/2),2)+pow(Y-(H/2),2),pow(min(W/2,H/2),2)),255,0)':g='if(lte(pow(X-(W/2),2)+pow(Y-(H/2),2),pow(min(W/2,H/2),2)),255,0)':b='if(lte(pow(X-(W/2),2)+pow(Y-(H/2),2),pow(min(W/2,H/2),2)),255,0)':a=255[alpha_mask];
    # [base][alpha_mask]alphamerge
    
    # Wait, 'geq' operates on YUV or RGB planes depending on format.
    # For RGBA, we can control alpha directly if supported, or use 'alphamerge'.
    # Let's try creating a mask using 'geq' on a separate greyscale stream.
    
    command_png = [
        "ffmpeg", "-y",
        "-i", input_image,
        "-filter_complex",
        "[0:v]format=rgba[base];"
        "[base]split[img][img2];"
        "[img2]format=gray,geq='if(lte(pow(X-(W/2),2)+pow(Y-(H/2),2),pow(min(W/2,H/2)-2,2)),255,0)'[mask];"
        "[img][mask]alphamerge",
        output_png
    ]
    
    print(f"Generating circular PNG: {output_png}")
    try:
        subprocess.run(command_png, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("  Success!")
    except subprocess.CalledProcessError as e:
        print(f"  Error: {e.stderr.decode()}")
        # Fallback debug
        print("  Trying simple resize if mask fails (just to verify file access)...")
        return

    # 2. Generate ICO from circular PNG
    # Resize to 32x32 for favicon.ico
    command_ico = [
        "ffmpeg", "-y",
        "-i", output_png,
        "-vf", "scale=32:-1",
        output_ico
    ]
    
    print(f"Generating favicon.ico: {output_ico}")
    try:
        subprocess.run(command_ico, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("  Success!")
    except subprocess.CalledProcessError as e:
        print(f"  Error: {e.stderr.decode()}")

if __name__ == "__main__":
    generate_circular_favicon()
