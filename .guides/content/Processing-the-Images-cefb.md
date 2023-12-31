

Now that we have generated and downloaded the Earth images at different angles, it's time to process them and create a GIF animation. We'll be using the Python Imaging Library (PIL) to accomplish this.

First, let's resize the images so the animation is smaller in size and easier to handle. In the following code, we resize each image in the `earth_images` list to 256x256 pixels:
```python
angles = range(0, 360, 10)
image_filenames = [f"earth_{angle}_degrees.jpg" for angle in angles]

resized_earth_images = []
for filename in image_filenames:
    img = Image.open(filename)
    resized_img = img.resize((256, 256), Image.ANTIALIAS)
    resized_earth_images.append(resized_img)

```
{Try it}(python3 main.py 2)
We create a list of image filenames called `image_filenames` for the Earth images at different angles. We then create an empty list `resized_earth_images` to store the resized images. In the for loop, we open each image using its filename, resize it, and append it to the `resized_earth_images` list.


### Creating the GIF Animation

Next, we'll create a GIF animation using the resized images. We can do this using the `save` method of the PIL Image class. We'll set the duration of each frame to 100 milliseconds and loop the animation indefinitely:

```python
output_gif = "rotating_earth.gif"
resized_earth_images[0].save(
    output_gif,
    save_all=True,
    append_images=resized_earth_images[1:],
    duration=100,
    loop=0
)
```
{Try it}(python3 main.py 3)
In this code, we first specify the output GIF filename as `"rotating_earth.gif"`. Then, we call the save method on the first image in the `resized_earth_images` list. We set `save_all=True` to indicate that we want to save multiple frames. The `append_images` parameter is set to the rest of the images in the list, and we specify the duration and loop count using the `duration` and `loop` parameters, respectively.

Now, when you run this code, a GIF animation called "rotating_earth.gif" will be created, showcasing the Earth rotating using the images generated by the DALL-E 2 API.

![rotating_earth](rotating_earth.gif)
 
The images that the AI generated did not all look the same hence our current gif. The different images don't have the same center there fore our gif looks less smooth

**0 degrees**
![earth_0_degrees](earth_0_degrees.jpg)
**270 degrees**
![earth_270_degrees](earth_270_degrees.jpg)
**350 degrees**
![earth_350_degrees](earth_350_degrees.jpg)


{Check It!|assessment}(fill-in-the-blanks-1980393926)
