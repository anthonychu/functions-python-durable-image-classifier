import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    user_id = req.params['userid']
    
    client = df.DurableOrchestrationClient(starter)
    orchestration_input = {
        'user_id': user_id,
        'image_count': int(req.route_params["count"])
    }
    instance_id = await client.start_new('PetClassificationOrchestrator', None, orchestration_input)

    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    return client.create_check_status_response(req, instance_id)
