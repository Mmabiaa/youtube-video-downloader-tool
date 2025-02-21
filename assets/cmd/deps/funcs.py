import os
import re
from pytubefix import YouTube, Playlist
# moved download_video to funcs.py

#sanitize function to remove invalid characters from file names
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)


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
            caption = yt.captions.get('a.en')
            if caption is not None:
                print("Subtitles Available:")
                print("Downloading subtitles...")
                try:
                    sanitize_title = sanitize_filename(yt.title) #remove invalid characters from file name
                    caption_filename = f"{sanitize_title}_captions.srt"
                    srt_captions = caption.generate_srt_captions()
                    with open(os.path.join(download_path, caption_filename), 'w', encoding='utf-8') as f:
                        f.write(srt_captions)
                    print(f"Subtitle for {yt.captions} downloaded to: {download_path}")
                except Exception as e:
                    print(f"Error downloading {yt.captions} subtitle: {e}")

            else:
                print("No Available subtitles")
            
        print("Download complete.")
        return 1
    except KeyboardInterrupt:
        print("Aborted download.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1