from asyncio import sleep
import json
import logging
from os import environ
from random import choice

import azure.functions as func
from .predict import predict_image_from_url


async def main(request: dict, signalr: func.Out[str]) -> str:
    try:
        image_id = request['image_id']
        image_url = environ['ImagesBaseUrl'] + image_id
        user_id = request['user_id']

        results = predict_image_from_url(image_url)
        prediction = results['predictedTagName']
        logging.info(prediction + ' - ' + image_id)
    except:
        logging.error('Failed to classify ' + image_id)
        prediction = 'unknown'
    
    signalr_message = {
        'target': 'newImageResult',
        'userId': user_id,
        'arguments': [{
            'imageUrl': image_url,
            'prediction': prediction
        }]
    }
    signalr.set(json.dumps(signalr_message))
    return prediction
