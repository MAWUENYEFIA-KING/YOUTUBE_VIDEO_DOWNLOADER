
import yt_dlp

def download_youtube_video():
    url = input("Enter the YouTube video URL: ").strip()

    print("Downloading highest quality video...")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("✅ Download completed successfully!")

if __name__ == "__main__":
    download_youtube_video()
