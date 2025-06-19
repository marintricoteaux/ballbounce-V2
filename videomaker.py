import time
import os
import glob
from moviepy import ImageSequenceClip

def makeVideo():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    os.makedirs("videos", exist_ok=True)
    filename = os.path.join("videos", f"simulation_{timestamp}.mp4")

    clip = ImageSequenceClip("frames", fps=60)
    clip.write_videofile(filename, codec="libx264")

def cleanFrames():
    for file in glob.glob("frames/*.png"):
        os.remove(file)