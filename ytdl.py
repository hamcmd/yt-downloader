import subprocess
# import argparse

def download_video_segment(url, start_time, end_time, output_file=None):
    """
    Download a specific segment of a video using yt-dlp

    Parameters:
    url (str): URL of the video
    start_time (str): Start time in HH:MM:SS format
    end_time (str): End time in HH:MM:SS format
    output_file (str): Optional output filename
    """

    # Build the download command
    command = [
        'yt-dlp',
        '--download-sections',
        f'*{start_time}-{end_time}',
        # Force MP4 container
        '--format', 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        # Merge video and audio, force MP4 with H.264 video and AAC audio
        '--merge-output-format', 'mp4',
        # Additional parameters for PowerPoint compatibility
        '--postprocessor-args', 'ffmpeg:-c:v libx264 -c:a aac -strict experimental -b:a 192k -ar 48000',
        '-o', output_file,
        url
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Successfully downloaded video segment from {start_time} to {end_time}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Download a specific segment of a video using yt-dlp")
#     parser.add_argument("url", help="URL of the video")
#     parser.add_argument("start_time", help="Start time in HH:MM:SS format")
#     parser.add_argument("end_time", help="End time in HH:MM:SS format")
#     parser.add_argument("-o", "--output", help="Output filename", default=None)

#     args = parser.parse_args()
#     download_video_segment(args.url, args.start_time, args.end_time, args.output)


download_video_segment(
    "https://youtu.be/DHnHpHkwqs4",
    "00:00:00",
    "00:03:05",
    "output.mp4"
)
