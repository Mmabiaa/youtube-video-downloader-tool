from deps.funcs import download_video 
import argparse
# changed usable library to pytubefix since YEAH

def main() -> None:
    # added argument parser
    parser = argparse.ArgumentParser(description="Download a YouTube video.")
    parser.add_argument("video_url", help="The URL of the YouTube video.")
    parser.add_argument("--path", help="The path to download the video to.")
    parser.add_argument("--only_audio", help="Download audio only.", action="store_true")
    parser.add_argument("--subtitles", help="Download subtitles.", action="store_true")
    parser.add_argument("--playlist", help="Download a playlist.", action="store_true")
    args = parser.parse_args()
    download_video(args.video_url, args.path, args.only_audio, args.subtitles, args.playlist)

if __name__ == "__main__":
    main()
