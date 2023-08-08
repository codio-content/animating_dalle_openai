# CODIO SOLUTION BEGIN
import os
import openai
from PIL import Image, ImageOps,ImageChops
from io import BytesIO
import requests

# Set environment variables
openai.api_key =  os.getenv('OPENAI_KEY')

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

def download_image(image_url,x):
    response = requests.get(image_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    with open(x+'.jpg', 'wb') as handler:
      handler.write(img_data)
    return img


angles = range(0, 360, 10)
image_filenames = [f"earth_{angle}_degrees.jpg" for angle in angles]

resized_earth_images = []
for filename in image_filenames:
    img = Image.open(filename)
    resized_img = img.resize((256, 256), Image.ANTIALIAS)
    resized_earth_images.append(resized_img)

output_gif = "rotating_earth.gif"
resized_earth_images[0].save(
    output_gif,
    save_all=True,
    append_images=resized_earth_images[1:],
    duration=400,
    loop=0
)

duration = 200  # Adjust the frame duration to your preference
loop_count = 3  # Adjust the loop count to your preference
optimize = True  # Enable image optimization



output_gif = "optimized_rotating_earth.gif"
resized_earth_images[0].save(
    output_gif,
    save_all=True,
    append_images=resized_earth_images[1:],
    duration=200,
    loop=3,
    optimize=True
)
from PIL import ImageChops

def crossfade(image1, image2, alpha):
    return ImageChops.blend(image1, image2, alpha)

crossfade_frames = []
for i in range(len(resized_earth_images) - 1):
    for alpha in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
        frame = crossfade(resized_earth_images[i], resized_earth_images[i + 1], alpha)
        crossfade_frames.append(frame)
from PIL import ImageEnhance

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

brightness_factor = 1.5
brightened_frames = [adjust_brightness(frame, brightness_factor) for frame in crossfade_frames]
output_gif = "enhanced_rotating_earth.gif"
brightened_frames[0].save(
    output_gif,
    save_all=True,
    append_images=brightened_frames[1:],
    duration=duration,
    loop=loop_count,
    optimize=optimize
)
# CODIO SOLUTION END