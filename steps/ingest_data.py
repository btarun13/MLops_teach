import logging
import pandas as pd
from zenml import step


class IngestData:
    """
    Ingests data from a given path
    """
    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
        logging.info(f"ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingests data from a given path,

    Args:
        data_path: Path to the data
    Returns:
        pd.DataFrame: The ingested data
    """

    try:
        ingestter = IngestData(data_path)
        df = ingestter.get_data()
        return df
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")
        return e