import cv2
import os
from PIL import Image
from to_byte_arr import to_byte_arr, hacky_final_output
from crop_image import crop_image

video_path = 'shrek.mp4'
output_folder = 'frames'
desired_frames = (60 * 24) - 4

image_dimen = (300, 200)  # Image width, height
image_quality = 30

# Crop details should be smaller than then the above
should_crop_image = True
crop_dimen = (200, 200)  # Cropped image width, height

in_colour = False

output_byte_arr = True
output_text_file = "frames.h"
output_prefix = "f"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if output_byte_arr:
    open(output_text_file, "w").close()

print("Reading Video...")
video = cv2.VideoCapture(video_path)

print("Reading Metadata...")
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

count = jump = int(total_frames / desired_frames)
video.set(cv2.CAP_PROP_POS_FRAMES, count)

print(f"Total Frames:'{total_frames}' & Frame Interval:'{jump}'")

print("Running...")

time_checker = 0

while video.isOpened():
    ret, frame = video.read()

    if ret:
        image = None

        if in_colour:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

        image = image.resize(image_dimen)

        if should_crop_image:
            image = crop_image(image, image_dimen, crop_dimen)

        '''
        image = image.convert('L')
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)

        image = image.convert('1')
        '''

        if output_byte_arr:
            to_byte_arr(image, crop_dimen if output_byte_arr else image_dimen, output_text_file, output_prefix)
        else:
            output_path = os.path.join(output_folder, f'frame_{count:04d}.jpg')
            image.save(output_path, quality=image_quality)

        count += jump
        video.set(cv2.CAP_PROP_POS_FRAMES, count)

        time_checker += 1

        if time_checker > 10:
            time_checker = 0
            print(f"Frame {count} of {total_frames}")


    else:
        video.release()
        break

# A hacky output for the byte array code
if output_byte_arr:
    hacky_final_output(output_text_file, desired_frames)

print("Run Complete...")
