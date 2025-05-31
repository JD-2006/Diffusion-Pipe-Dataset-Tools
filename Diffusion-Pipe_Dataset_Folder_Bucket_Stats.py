import os
import subprocess
import json
from PIL import Image

def get_media_files(folder):
    video_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.webm')
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')

    files = os.listdir(folder)
    videos = sorted([os.path.join(folder, f) for f in files if f.lower().endswith(video_extensions)])
    images = [os.path.join(folder, f) for f in files if f.lower().endswith(image_extensions)]

    return videos, images

def get_video_resolution_and_frames(path):
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error',
             '-select_streams', 'v:0',
             '-show_entries', 'stream=width,height,nb_frames',
             '-of', 'json', path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        info = json.loads(result.stdout)
        stream = info['streams'][0]
        width = int(stream['width'])
        height = int(stream['height'])

        frame_count = stream.get('nb_frames')
        if frame_count is None or not frame_count.isdigit():
            result = subprocess.run(
                ['ffprobe', '-v', 'error',
                 '-count_frames',
                 '-select_streams', 'v:0',
                 '-show_entries', 'stream=nb_read_frames',
                 '-of', 'default=nokey=1:noprint_wrappers=1', path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            frame_count = result.stdout.strip()

        count = int(frame_count) if frame_count.isdigit() else 1
        return width, height, count
    except Exception as e:
        print(f"⚠️ Video error: {path} -> {e}")
        return None

def get_image_resolution(path):
    try:
        with Image.open(path) as img:
            return img.width, img.height
    except Exception as e:
        print(f"⚠️ Image error: {path} -> {e}")
        return None

def main():
    folder = input("Enter the full path to the folder of videos/images: ").strip()

    if not os.path.exists(folder):
        print("❌ Folder does not exist.")
        return

    videos, images = get_media_files(folder)
    if not videos and not images:
        print("❌ No media files found in the folder.")
        return

    entries = []

    print("\n📼 Per-video output:")
    print("------------------------")

    for video in videos:
        res = get_video_resolution_and_frames(video)
        if res:
            w, h, count = res
            print(f"{os.path.basename(video)} -> [{w}, {h}, {count}]")
            entries.append([w, h, count])

    for image in images:
        res = get_image_resolution(image)
        if res:
            w, h = res
            entries.append([w, h, 1])

    output_path = os.path.join(folder, "size_buckets.txt")

    with open(output_path, "w") as f:
        f.write("size_buckets = [\n")
        for w, h, n in entries:
            f.write(f"    [{w}, {h}, {n}],\n")
        f.write("]\n")

    print("\n✅ size_buckets written to:", output_path)

if __name__ == "__main__":
    main()
