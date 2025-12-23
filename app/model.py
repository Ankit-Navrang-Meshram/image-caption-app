from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 1. Load the model globally so it doesn't reload on every request
# We use the 'base' version of BLIP which is fast and lightweight.
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image: Image.Image):
    """
    Takes a PIL Image and returns a string caption.
    """
    # Prepare the image
    inputs = processor(image, return_tensors="pt")

    # Generate output
    out = model.generate(**inputs)

    # Decode the output to text
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption