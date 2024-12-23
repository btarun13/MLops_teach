import logging
from zenml import step
import pandas as pd

@step
def evaluate_model(df: pd.DataFrame) -> None:
    """
    Evaluates the model
    Args:
        df: The ingested data
    """
    # logging.info("Evaluating model")
    # Evaluate model here
    pass