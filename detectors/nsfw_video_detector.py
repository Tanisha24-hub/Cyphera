import os
import cv2
from tqdm import tqdm
from nudenet import NudeDetector

def extract_and_classify_frames(video_path, output_folder, interval, nsfw_threshold):
    cap = cv2.VideoCapture(video_path)
    detector = NudeDetector()
    os.makedirs(output_folder, exist_ok=True)
    nsfw = []
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_num = 0
    with tqdm(total=total) as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_num % interval == 0:
                path = os.path.join(output_folder, f"frame_{frame_num}.jpg")
                cv2.imwrite(path, frame)
                result = detector.detect(path)
                if result and result[0]['label'] == 'unsafe':
                    if result[0]['unsafe'] > nsfw_threshold:
                        nsfw.append((frame_num, result[0]['unsafe']))
            frame_num += 1
            pbar.update(1)
    cap.release()
    return nsfw
