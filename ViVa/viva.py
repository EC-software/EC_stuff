import os
import moviepy
# from moviepy.editor import VideoFileClip

def list_and_extract_metadata(directory):
    # List all .mp4 files in the directory
    mp4_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]

    # Extract metadata for each .mp4 file
    metadata = []
    for file in mp4_files:
        file_path = os.path.join(directory, file)
        try:
            with moviepy.VideoFileClip(file_path) as video:
                duration = video.duration  # Duration in seconds
                fps = video.fps            # Frames per second
                size = video.size          # (width, height)
                codec = video.reader.codec # Video codec
                bitrate = video.reader.bitrate if hasattr(video.reader, 'bitrate') else 'N/A' # Bitrate
                audio_codec = video.audio.codec if video.audio else 'N/A' # Audio codec

                metadata.append({
                    'filename': file,
                    'duration': duration,
                    'fps': fps,
                    'size': size,
                    'video_codec': codec,
                    'bitrate': bitrate,
                    'audio_codec': audio_codec
                })
        except Exception as e:
            print(f"Error processing {file}: {e}")

    return metadata

# Example usage
# directory = '/path/to/your/directory'  # Replace with your directory path
directory = '/csmsp/.TMP/1_NEWS/1212/GoodAndBad'  # Replace with your directory path
metadata = list_and_extract_metadata(directory)

# Print the metadata
for meta in metadata:
    print(f"File: {meta['filename']}")
    print(f"  Duration: {meta['duration']} seconds")
    print(f"  FPS: {meta['fps']}")
    print(f"  Size: {meta['size']}")
    print(f"  Video Codec: {meta['video_codec']}")
    print(f"  Bitrate: {meta['bitrate']}")
    print(f"  Audio Codec: {meta['audio_codec']}")
    print()
