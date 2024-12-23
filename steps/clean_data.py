import logging
import pandas as pd
from zenml import step


@step
def clean_df(df: pd.DataFrame) -> None:
    """
    Cleans the data by removing NaNs

    Args:
        df: The input DataFrame
    Returns:
        pd.DataFrame: The cleaned DataFrame
    """

    # logging.info("Cleaning data")
    # return df.dropna()
    pass