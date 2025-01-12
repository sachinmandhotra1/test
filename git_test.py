from prefect import flow, task
from prefect.cache_policies import NONE
from datetime import datetime


@task(log_prints=True, cache_policy=NONE)
def orchestrate_entity_workflow(entity_to_process=None, input_data=None):
    """
    Orchestrates the workflow for processing an entity and its related entities.

    Parameters
    ----------
    entity_to_process : str
        The name of the entity to be processed.
    input_data : dict
        A dictionary containing the data to be inserted for the entity.

    Returns
    -------
    None
    """
    print(f"========= START TIME -> {datetime.now()} =========")
    print(f"Processing entity - '{entity_to_process}'...")


    print(f"Processed entity - '{entity_to_process}' successfully.")
    print(f"========= END TIME -> {datetime.now()} =========")


@flow(log_prints=True)
def main(entity_to_process, input_data):
    orchestrate_entity_workflow(entity_to_process, input_data)
