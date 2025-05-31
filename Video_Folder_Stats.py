import os
import cv2

def get_video_metadata(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return width, height, fps, frame_count

def main():
    print("Please enter the full path to the folder containing your video clips.")
    folder_path = input("Folder path: ").strip().strip('"').strip("'")

    if not os.path.isdir(folder_path):
        print("❌ That path does not exist or is not a folder.")
        return

    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm')
    video_files = [f for f in os.listdir(folder_path) if f.lower().endswith(video_extensions)]

#    # Sort by file modification time (most consistent with file explorer order)
#    video_files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))
     # Sort by file alphabetically
    video_files.sort(key=str.lower)

    output_lines = []

    for video in video_files:
        path = os.path.join(folder_path, video)
        metadata = get_video_metadata(path)
        if metadata:
            width, height, fps, frame_count = metadata
            line = f"{video}, {width}x{height}, {fps:.2f} fps, {frame_count} frames"
        else:
            line = f"{video}, Error reading video"
        output_lines.append(line)

    folder_name = os.path.basename(os.path.normpath(folder_path))
    output_path = os.path.join(folder_path, f"{folder_name}.txt")

    with open(output_path, 'w') as f:
        for line in output_lines:
            f.write(line + '\n')

    print(f"\n✅ Metadata exported to: {output_path}")

if __name__ == "__main__":
    main()
