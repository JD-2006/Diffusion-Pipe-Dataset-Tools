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

def get_video_resolution(path):
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error',
             '-select_streams', 'v:0',
             '-show_entries', 'stream=width,height',
             '-of', 'json', path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        info = json.loads(result.stdout)
        stream = info['streams'][0]
        width = int(stream['width'])
        height = int(stream['height'])
        return width, height
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

    print("\n🧾 Resolutions collected:")
    print("--------------------------")

    for video in videos:
        res = get_video_resolution(video)
        if res:
            w, h = res
            print(f"{os.path.basename(video)} -> [{w}, {h}]")
            entries.append([w, h])

    for image in images:
        res = get_image_resolution(image)
        if res:
            w, h = res
            entries.append([w, h])

    output_path = os.path.join(folder, "resolutions.txt")

    with open(output_path, "w") as f:
        f.write("resolutions = [\n")
        for w, h in entries:
            f.write(f"    [{w}, {h}],\n")
        f.write("]\n")

    print("\n✅ resolutions written to:", output_path)

if __name__ == "__main__":
    main()
