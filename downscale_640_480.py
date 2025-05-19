import os
import subprocess
import sys

# ─── CONFIG ───────────────────────────────────────────────────────────────────

# Change these two paths as needed:
INPUT_BASE  = r"C:\Users\Jeffr\Downloads\ultrasound\resize"
OUTPUT_BASE = r"C:\Users\Jeffr\Downloads\ultrasound\resize_output"

# JPEG quality: 2–31, lower means better quality/higher size.
JPEG_Q = "8"

# Desired output resolution
TARGET_W, TARGET_H = 640, 480

# ─── END CONFIG ────────────────────────────────────────────────────────────────

def convert_and_scale_to_jpg(src_path, dst_path):
    """
    Uses ffmpeg to convert src_path to dst_path (JPEG), scaling to TARGET_W×TARGET_H
    and applying a quality scale to reduce file size.
    """
    cmd = [
        "ffmpeg", "-y",
        "-i", src_path,
        "-vf", f"scale={TARGET_W}:{TARGET_H}",
        "-qscale:v", JPEG_Q,
        dst_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    for root, _, files in os.walk(INPUT_BASE):
        # compute relative path and corresponding output folder
        rel = os.path.relpath(root, INPUT_BASE)
        target_dir = os.path.join(OUTPUT_BASE, rel)
        os.makedirs(target_dir, exist_ok=True)

        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            # process common image formats
            if ext not in ('.png', '.jpg', '.jpeg', '.bmp', '.tiff'):
                continue

            src = os.path.join(root, fname)
            base = os.path.splitext(fname)[0]
            dst = os.path.join(target_dir, base + ".jpg")

            try:
                convert_and_scale_to_jpg(src, dst)
                print(f"✓ Converted & scaled: {src} → {dst}")
            except subprocess.CalledProcessError:
                print(f"✗ ffmpeg failed on: {src}", file=sys.stderr)

if __name__ == "__main__":
    main()
