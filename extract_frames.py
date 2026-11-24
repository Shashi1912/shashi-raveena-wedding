import cv2
import os
import glob

os.makedirs('reel_frames', exist_ok=True)

videos = glob.glob('*.mp4') + glob.glob('*.webm')
print("Found videos:", videos)

for v in videos:
    cap = cv2.VideoCapture(v)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    print(f"Video {v}: {fps} fps, {total_frames} frames, {duration:.1f}s")
    
    # Save frames every 1 second
    step = int(fps)
    count = 0
    saved = 0
    while cap.isOpened() and saved < 15:
        ret, frame = cap.read()
        if not ret:
            break
        if count % step == 0:
            out_name = f"reel_frames/{os.path.splitext(v)[0]}_sec{saved:02d}.jpg"
            cv2.imwrite(out_name, frame)
            saved += 1
        count += 1
    cap.release()
    print(f"Saved {saved} frames for {v}")
