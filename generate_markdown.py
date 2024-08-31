import os
import exifread
from datetime import datetime

# Path to your images directory
IMAGES_DIR = 'aidan-mckenzie/assets/imgs/gallery/'
OUTPUT_DIR = 'aidan-mckenzie/_gallery/'

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_exif_data(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)

    def get_printable(tag):
        if hasattr(tag, 'printable'):
            return tag.printable
        return tag

    def decode_exif_tag(tag):
        # Decode UTF-16 encoded EXIF tag
        if tag and isinstance(tag, str):
            return tag.strip('\x00')  # Remove any trailing null bytes
        return tag

    # Extract EXIF data
    title = decode_exif_tag(get_printable(tags.get('Image ImageDescription', 'Untitled')))
    artist = decode_exif_tag(get_printable(tags.get('Image Artist', '')))
    date_time = str(decode_exif_tag(get_printable(tags.get('EXIF DateTimeOriginal', ''))))
    date = datetime.strptime(date_time, "%Y:%m:%d %H:%M:%S")
    friendly_date = date.strftime("%a %d %b %Y")

    return {
        'title': title,
        'artist': artist,
        'date_time': friendly_date,
    }

def create_markdown(image_path, metadata):
    file_name = os.path.splitext(os.path.basename(image_path))[0] + '.md'
    markdown_path = os.path.join(OUTPUT_DIR, file_name)
    
    with open(markdown_path, 'w') as f:
        f.write('---\n')
        f.write(f'title: "{metadata["title"]}"\n')
        f.write(f'subtitle: "{metadata["artist"]}"\n')
        f.write(f'date_taken: "{metadata["date_time"]}"\n')
        f.write(f'image_path: "/assets/imgs/gallery/{os.path.basename(image_path)}"\n')
        f.write('---\n')

for root, _, files in os.walk(IMAGES_DIR):
    for file in files:
        if file.lower().endswith('.jpg'):
            image_path = os.path.join(root, file)
            metadata = extract_exif_data(image_path)
            create_markdown(image_path, metadata)

print("Markdown files generated successfully!")
