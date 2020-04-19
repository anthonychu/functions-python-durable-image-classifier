import logging
import json
from itertools import groupby

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    orchestration_input = json.loads(context.get_input())
    image_count = orchestration_input['image_count']

    image_ids_json = yield context.call_activity('GetImagesToClassify', image_count)
    image_ids = json.loads(image_ids_json)

    user_id = orchestration_input['user_id']
    tasks = [context.call_activity('ClassifyImage', {'user_id': user_id, 'image_id': i}) for i in image_ids]
    results = yield context.task_all(tasks)

    summary = {pet: len(list(freq)) for pet, freq in groupby(sorted(results))}
    return summary


main = df.Orchestrator.create(orchestrator_function)
