# CODIO SOLUTION BEGIN
import main
from PIL import Image
 
seasons = ['summer', 'autumn', 'winter', 'spring']
image_urls = []

for season in seasons:
    prompt = f"A well in the {season}"
    image_url = main.generate_base_image(prompt)
    image_urls.append(image_url)

image_filenames = []
for i, image_url in enumerate(image_urls):
    img = main.download_image(image_url, seasons[i])
    image_filenames.append(f"{seasons[i]}.jpg")

resized_images = []
for filename in image_filenames:
    img = Image.open(filename)
    resized_img = img.resize((256, 256), Image.ANTIALIAS)
    resized_images.append(resized_img)

output_gif = "well_seasons.gif"
resized_images[0].save(
    output_gif,
    save_all=True,
    append_images=resized_images[1:],
    duration=200,
    loop=4,
    optimize=True
)

# CODIO SOLUTION END