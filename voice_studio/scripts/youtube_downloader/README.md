# YouTube Segment Downloader

A fast and efficient tool to download specific segments from YouTube videos as MP3 files, without downloading the entire video first.

## Features

- ✅ Download only the segment you want (saves time and bandwidth)
- ✅ Direct MP3 conversion during download 
- ✅ Automatic filename generation from video title
- ✅ Multiple time format support
- ✅ High-quality audio extraction

## Requirements

- `yt-dlp` (installed ✅)
- `ffmpeg` (installed ✅)
- Python 3

## Usage

### Quick Method (Recommended)
```bash
./yt-clip "https://youtu.be/VIDEO_ID" "start_time" "end_time" [optional_name]
```

### Python Script Method
```bash
python3 yt-segment.py "https://youtu.be/VIDEO_ID" "start_time" "end_time" [optional_name]
```

## Examples

```bash
# Download 30 seconds to 1 minute 45 seconds
./yt-clip "https://youtu.be/dQw4w9WgXcQ" "0:30" "1:45"

# Download with custom filename
./yt-clip "https://youtu.be/dQw4w9WgXcQ" "1:20" "2:30" "best_part"

# Download using different time formats
./yt-clip "https://youtu.be/dQw4w9WgXcQ" "90" "150"        # seconds
./yt-clip "https://youtu.be/dQw4w9WgXcQ" "1:30" "2:30"     # MM:SS
./yt-clip "https://youtu.be/dQw4w9WgXcQ" "0:01:30" "0:02:30" # HH:MM:SS
```

## Time Format Support

- **Seconds**: `90` (90 seconds)
- **MM:SS**: `1:30` (1 minute 30 seconds)  
- **HH:MM:SS**: `0:01:30` (1 minute 30 seconds)

## Output

- Files are saved as `{video_title}_{start}-{end}.mp3`
- Or with custom name: `{custom_name}.mp3`
- High quality MP3 format
- Shows download progress and final file size

## Why This is Better

**Before**: Download entire 1-hour video → Extract segment → Convert to MP3  
**Now**: Download only the 2-minute segment you want as MP3 directly

This saves significant time, bandwidth, and storage space! 