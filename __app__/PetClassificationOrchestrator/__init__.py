import logging
import json
from itertools import groupby

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    num_images = int(context.get_input())
    image_ids_json = yield context.call_activity('GetImagesToProcess', num_images)
    image_ids = json.loads(image_ids_json)

    tasks = [context.call_activity('ProcessImage', i) for i in image_ids]
    results = yield context.task_all(tasks)

    summary = {pet: len(list(freq)) for pet, freq in groupby(sorted(results))}
    return summary


main = df.Orchestrator.create(orchestrator_function)
