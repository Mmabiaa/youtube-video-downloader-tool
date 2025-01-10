import os
from pytube import YouTube

def download_video(video_url, download_path, download_audio=False, download_subtitles=False):
    try:
        yt = YouTube(video_url)
        print(f"Downloading '{yt.title}'...")

        if download_audio:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(download_path)
            print(f"Downloaded audio for '{yt.title}' successfully!")
        else:
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(download_path)
            print(f"Downloaded video '{yt.title}' successfully!")

        if download_subtitles:
            caption = yt.captions.get_by_language_code('en')
            if caption:
                caption.download(download_path)
                print(f"Downloaded subtitles for '{yt.title}' successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave blank for current directory): ")
    
    if not download_path:
        download_path = os.getcwd()

    download_audio = input("Download audio only? (y/n): ").lower() == 'y'
    download_subtitles = input("Download subtitles? (y/n): ").lower() == 'y'

    download_video(video_url, download_path, download_audio, download_subtitles)

if __name__ == "__main__":
    main()
