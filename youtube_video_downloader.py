import subprocess

def download_youtube_video():
    url = input("Enter the YouTube video URL: ").strip()

    try:
        print("Downloading highest quality video...")

        command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "--merge-output-format", "mp4",
            "--no-playlist",
            url
        ]

        subprocess.run(command, check=True)
        print("✅ Download completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred while downloading: {e}")

if __name__ == "__main__":
    download_youtube_video()
