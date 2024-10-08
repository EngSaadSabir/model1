# -*- coding: utf-8 -*-
"""MODEL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1drpNgIapfgBzz8gYiJdid9N6WeaGWOx_
"""

!pip install diffusers transformers torch

import torch
from diffusers import DiffusionPipeline
from PIL import Image

# Load the Stable Diffusion pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"
pipeline = DiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

# Function to generate an image
def generate_image(prompt, num_inference_steps=50):
    with torch.no_grad():
        output = pipeline(prompt, num_inference_steps=num_inference_steps)
        image = output.images[0]  # Adjusted to match the correct key
        return image

# Example prompt
prompt = "hotel in green mountain "
image = generate_image(prompt)

# Display the generated image
image.show()



image.save("generated_image.png")
from google.colab import files
files.download("generated_image.png")