from asyncio import sleep
import logging
from random import choice

from .predict import predict_image_from_url


async def main(imageId: str) -> str:
    try:
        image_url = 'https://pythonqueueimage.blob.core.windows.net/images/' + imageId
        results = predict_image_from_url(image_url)
        prediction = results['predictedTagName']
        logging.info(prediction + ' - ' + imageId)
    except:
        logging.error('Failed to classify ' + imageId)
        prediction = 'unknown'
        
    return prediction
