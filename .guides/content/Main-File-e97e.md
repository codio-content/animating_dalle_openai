Before we start, we are going to create a main file with some functions. This way we can use the functions across different files. This way we have access to all our libraries, API keys and image generation file. 

```python
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


```
{Try it}(python3 main.py)
This script essentially provides the functionality to generate an image based on a text prompt using the OpenAI API and then download and save that image to the local file system.

Now in all files we can just `import main` and we will have access to our library and functions. 


{Check It!|assessment}(multiple-choice-2699972370)
