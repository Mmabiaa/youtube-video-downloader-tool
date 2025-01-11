import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
# moved download_video to funcs.py
# function returns 1 if download is successful, 0 if aborted, -1 if error


def download_video(video_url, download_path, download_audio=False, download_subtitles=False, download_playlist=False, handle_flag=False) -> int:
    try:
        if not download_path:
            download_path = os.getcwd()

        # repeat whith each video in the playlist, if it is selected
        if download_playlist:
            pl = Playlist(video_url)
            # create a folder for the playlist
            download_path = os.path.join(download_path, pl.title)
            os.makedirs(download_path, exist_ok=True)
            print(f"Downloading playlist {pl.title}, of {len(pl.videos)} videos...")
            print("----------------------------------------")
            for video in pl.videos:
                if download_video(video, download_path, download_audio, download_subtitles, handle_flag=True) == 0:
                    break
            print("----------------------------------------")
            print("Download complete.")
            return

        # use hanfle flag to determine if the video_url is a YouTube object or a string
        if not handle_flag:
            yt = YouTube(video_url)
        else:
            yt = video_url
        print(f"Downloading '{yt.title}'...")

        if download_audio:
            audio_stream = yt.streams.get_audio_only()
            audio_stream.download(download_path)
        else:
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(download_path)
        
        if download_subtitles:
            subtitles = yt.captions
            print(subtitles)
            for lang in subtitles:
                caption = subtitles[lang]
                caption.download(download_path)
        print("Download complete.")
        return 1
    except KeyboardInterrupt:
        print("Aborted download.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1