import cv2
import os

def extract_keyframes(video_path, output_folder, num_frames):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = cv2.VideoCapture(video_path)

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_interval = max(1, total_frames // num_frames)

    current_frame = 0

    while current_frame < total_frames:
        ret, frame = video.read()
        if not ret:
            break
        if current_frame % frame_interval == 0:
            output_path = os.path.join(output_folder, f"frame{current_frame}.jpg")
            cv2.imwrite(output_path, frame)
        current_frame += 1

        if current_frame >= num_frames:
            break
    video.release()
    cv2.destroyAllWindows()

    return min(num_frames, current_frame)

