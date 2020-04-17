from asyncio import sleep
import logging
from random import choice

from .predict import predict_image_from_url


async def main(imageId: str) -> str:
    image_url = 'https://pythonqueueimage.blob.core.windows.net/images/' + imageId
    result = predict_image_from_url(image_url)
    logging.info(result['predictedTagName'] + ' - ' + imageId)
    return result['predictedTagName']
