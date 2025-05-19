import os
import subprocess

# Define the input folder where the .MOV files are located
input_folder = '..\input'

# Get all .MOV files in the input folder
mov_files = [f for f in os.listdir(input_folder) if f.endswith('.MOV')]

# Process each .MOV file
for mov_file in mov_files:
    # Create a directory for each .MOV file (if not already exists)
    file_name_without_extension = os.path.splitext(mov_file)[0]
    output_dir = os.path.join(input_folder, file_name_without_extension)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Set the input and output paths for FFmpeg
    input_path = os.path.join(input_folder, mov_file)
    output_path = os.path.join(output_dir, 'frame_%04d.jpg')  # Frames will be saved as JPEG images
    
    # FFmpeg command to extract every even frame
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_path,  # Input video file
        '-vf', 'select=not(mod(n\,2))',  # Select every even frame (mod(n,2) == 0)
        '-vsync', 'vfr',    # Variable frame rate to avoid duplicating frames
        '-q:v', '2',        # Set the quality of the extracted frames (lower value is higher quality)
        output_path
    ]
    
    # Run FFmpeg command
    subprocess.run(ffmpeg_command)

    print(f"Even frames extracted for {mov_file} and saved to {output_dir}")
