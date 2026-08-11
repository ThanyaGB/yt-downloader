import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, path):
    # Options to extract information without downloading first
    ydl_opts_info = {'quiet': True}
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            # Fetch video metadata
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'video')
            formats = info.get('formats', [])

            # Filter for "combined" streams (video + audio in one file)
            # Similar to pytube's progressive=True
            available_streams = []
            for f in formats:
                if f.get('vcodec') != 'none' and f.get('acodec') != 'none' and f.get('ext') == 'mp4':
                    available_streams.append(f)

            print(f"\nTitle: {title}")
            print("Available MP4 Streams (Video + Audio):")
            
            # Display streams to user
            for i, f in enumerate(available_streams):
                size = f.get('filesize')
                size_str = f"{size / (1024*1024):.2f} MB" if size else "Unknown size"
                print(f"[{i}] Resolution: {f.get('resolution')} | Format ID: {f.get('format_id')} | Size: {size_str}")

            # Selection logic
            choice = input("\nEnter the index number [e.g., 0] to download: ")
            if choice.isdigit() and int(choice) < len(available_streams):
                selected_format = available_streams[int(choice)]['format_id']
                
                # Setup download options
                ydl_opts_download = {
                    'format': selected_format,
                    'outtmpl': f'{path}/%(title)s.%(ext)s',
                }
                
                print("Downloading...")
                with yt_dlp.YoutubeDL(ydl_opts_download) as ydl_down:
                    ydl_down.download([url])
                print("\nDownload completed!")
            else:
                print("Invalid selection.")

    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    return path

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = open_file_dialog()

    if download_path:
        download_video(video_url, download_path)
    else:
        print("No directory selected. Exiting...")






'''from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, path):
    try:
        yt = YouTube(url)
        print(f"Video Title: {yt.title}")
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        # Create a dictionary to store stream information for easy access
        streams_dict = {
            stream.itag:{
                'resolution': stream.resolution,
                'filesize': round(stream.filesize_mb, 2)
            }
            for stream in streams
        }
        # Display available streams to the user
        print("Available streams:")
        for tag in streams_dict.keys():
            # Display itag, resolution, and filesize for each stream
            print(tag, ":", streams_dict[tag]['resolution'], f"({streams_dict[tag]['filesize']} MB)")
        # Prompt the user to select an itag
        selected_itag = int(input("Enter the desired itag (e.g., 22): "))
        
        if selected_itag in streams_dict:
            # Download the selected stream
            stream = yt.streams.get_by_itag(selected_itag)
            stream.download(output_path=path)
            print("Download completed!")
        else:
            print("Selected itag not available.")

    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    path = filedialog.askdirectory()
    if path:
        print(f"Selected download path: {path}")
    return path

if __name__ == "__main__":
    # Create a simple GUI to select the download path
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    url = input("Enter the YouTube video URL: ")
    path = open_file_dialog()

    if path:
        print("Starting download...")
        download_video(url, path)
    else:
        print("No download path selected. Exiting...")





'''