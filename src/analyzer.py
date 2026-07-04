import cv2
import librosa
import os

def analyze_media_file(file_path):
    print(f"[*] Target selected for analysis: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"[!] Error: File '{file_path}' not found yet. Please add a test file to your data folder.")
        return

    # 1. VIDEO ANALYSIS: Open the video file using OpenCV
    video = cv2.VideoCapture(file_path)
    
    # Extract metadata metrics
    fps = video.get(cv2.CAP_PROP_FPS)          # Frames per second
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) # Total pictures in the video
    duration = total_frames / fps if fps > 0 else 0
    
    print(f"[✓] Video Stream Data:")
    print(f"    - Frames Per Second (FPS): {fps:.2f}")
    print(f"    - Total Video Frames: {int(total_frames)}")
    print(f"    - Duration: {duration:.2f} seconds")
    video.release()

    # 2. AUDIO ANALYSIS: Open the sound track using Librosa
    print("[*] Extracting audio frequencies...")
    # Loading just the first 10 seconds of audio to save processing power
    audio_data, sample_rate = librosa.load(file_path, duration=10)
    print(f"Audio Stream Data:")
    print(f"    - Sample Rate: {sample_rate} Hz (Data points per second)")
    print(f"    - Audio Array Shape: {audio_data.shape}")

# Running the analyzer on a placeholder file inside your new data directory
analyze_media_file("data/sample_video.mp4")