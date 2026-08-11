# YouTube Video Downloader CLI

A simple Python command-line utility built with `yt-dlp` and `tkinter` that lets you inspect available progressive MP4 formats (combined video and audio) for a given YouTube URL and download your chosen resolution to a destination folder.

---

## Features

* **Interactive Stream Selection:** Displays available single-file MP4 formats along with resolution, format ID, and estimated file size before downloading.
* ** graphical Folder Picker:** Opens a native GUI file dialog to select your download directory.
* **Metadata Extraction:** Fetches video titles and available formats without downloading the video file first.

---

## Prerequisites

* **Python 3.7+**
* **Tkinter System Package:** Tkinter comes pre-installed with standard Python distributions on Windows and macOS. If you are on Linux (e.g., Ubuntu/Debian), install it via your package manager if it isn't available:
  ```bash
  sudo apt-get install python3-tk
  ```

---

## Setup & Installation

1. **Clone or download** this repository.

2. **Install dependencies:**
   Run the following command to install the exact packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Use

1. **Run the script:**
   ```bash
   python main.py
   ```

2. **Provide a YouTube URL:** Paste the link into the console when prompted.
   ```text
   Enter the YouTube video URL: https://www.youtube.com/watch?v=EXAMPLE
   ```

3. **Choose a Destination Directory:** A GUI folder picker will appear. Select the folder where you want to save your file.

4. **Select Resolution:** The terminal will output all combined MP4 streams. Input the index number corresponding to your preferred stream:
   ```text
   Title: Sample Video Title
   Available MP4 Streams (Video + Audio):
   [0] Resolution: 640x360 | Format ID: 18 | Size: 14.20 MB
   [1] Resolution: 1280x720 | Format ID: 22 | Size: 48.50 MB

   Enter the index number [e.g., 0] to download: 1
   ```

5. **Completion:** The downloaded file will be saved inside your chosen folder formatted as `<Video Title>.mp4`.

---

## Technical Notes

* **Progressive MP4 Filter:** YouTube separates high-resolution video streams (1080p and higher) into individual video-only and audio-only streams. To avoid requiring external dependencies like `FFmpeg` to merge separate streams, this script specifically filters for pre-combined progressive streams (`vcodec != 'none'` and `acodec != 'none'`).
