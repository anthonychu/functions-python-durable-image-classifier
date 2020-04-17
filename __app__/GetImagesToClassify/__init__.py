from json import dumps
from random import sample, choice


def main(numImages: str) -> str:
    max_len = 1000
    num_images = int(numImages)
    if num_images > max_len:
        num_images = max_len
    elif num_images < 1:
        num_images = 1
    
    image_ids = sample(range(1000), int(num_images))
    return dumps([f"{choice(['Cat', 'Dog'])}/{i}.jpg" for i in image_ids])
