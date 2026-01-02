import time
from PIL import Image

def convert_ppm_to_jpeg(ppm_path, jpeg_path, quality=95, optimize=True):
    """Convert PPM image to JPEG format and return the time taken."""
    start_time = time.perf_counter()  # More precise than time.time()

    # Open and convert in one pass, let PIL handle it efficiently
    with Image.open(ppm_path) as img:
        # Convert to RGB if needed (in case of different modes)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save with optimization enabled
        img.save(jpeg_path, 'JPEG', quality=quality, optimize=optimize)

    end_time = time.perf_counter()
    time_taken = end_time - start_time

    return time_taken

if __name__ == "__main__":
    ppm_file = "image.ppm"
    jpeg_file = "image.jpg"

    time_taken = convert_ppm_to_jpeg(ppm_file, jpeg_file)

    print(f"Conversion complete!")
    print(f"Input: {ppm_file}")
    print(f"Output: {jpeg_file}")
    print(f"Time taken: {time_taken:.6f} seconds ({time_taken*1000:.2f} ms)")