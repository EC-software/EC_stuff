import ffmpeg
import os

def check_vlc_compatibility(directory):
    # List all .mp4 files in the directory
    # mp4_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]
    mp4_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]


    # Check compatibility for each .mp4 file
    compatibility = []
    for file in mp4_files:
        file_path = os.path.join(directory, file)
        try:
            # Extract metadata using ffprobe
            probe = ffmpeg.probe(file_path)
            video_info = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            audio_info = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)

            # Extract relevant attributes
            video_codec = video_info['codec_name'] if video_info else 'N/A'
            audio_codec = audio_info['codec_name'] if audio_info else 'N/A'
            container_format = probe['format']['format_name']

            # Assess compatibility
            is_video_codec_supported = video_codec in ['h264', 'hevc', 'mpeg4', 'vp8', 'vp9']
            is_audio_codec_supported = audio_codec in ['aac', 'mp3', 'ac3', 'flac', 'vorbis']
            is_container_supported = container_format == 'mp4'

            compatibility.append({
                'filename': file,
                'video_codec': video_codec,
                'audio_codec': audio_codec,
                'container_format': container_format,
                'is_video_codec_supported': is_video_codec_supported,
                'is_audio_codec_supported': is_audio_codec_supported,
                'is_container_supported': is_container_supported,
                'likely_playable_in_vlc': is_video_codec_supported and is_audio_codec_supported and is_container_supported
            })
        except Exception as e:
            print(f"Error processing {file}: {e}")

    return compatibility

# Example usage
directory = '/csmsp'  # Replace with your directory path
compatibility = check_vlc_compatibility(directory)

# Print the compatibility assessment
for result in compatibility:
    print(f"File: {result['filename']}")
    print(f"  Video Codec: {result['video_codec']} (Supported: {result['is_video_codec_supported']})")
    print(f"  Audio Codec: {result['audio_codec']} (Supported: {result['is_audio_codec_supported']})")
    print(f"  Container: {result['container_format']} (Supported: {result['is_container_supported']})")
    print(f"  Likely Playable in VLC: {result['likely_playable_in_vlc']}")
    print()
