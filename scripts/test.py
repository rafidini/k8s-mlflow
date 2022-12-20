# info: docker exec 824c383d0c84 python scripts/test.py
import os
from random import random, randint
from mlflow import log_metrics, log_params, log_artifacts,\
                   set_experiment,  log_dict, set_tracking_uri,\
                   get_tracking_uri

experiment: dict = {
    "parameters": {},
    "metrics": {}
}

if __name__ == "__main__":
    # Experiment name
    set_experiment('test')
    tracking_url: str = get_tracking_uri()
    print('URL:', tracking_url)

    # Prepare parameters + metrics
    for i in range(1, 5):
        experiment["parameters"][f"param{i}"] = randint(0, 100)
        experiment["metrics"][f"foo{i}"] = random()
    
    # Log an artifact (output file)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    # Log parameters + metrics
    log_params(experiment["parameters"])
    log_metrics(experiment["metrics"])

    # Save parameters / metrics
    log_dict(experiment, "experiment.json")
