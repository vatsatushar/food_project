from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = None
model = None


def load_blip():
    global processor, model

    if processor is None or model is None:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    return processor, model
