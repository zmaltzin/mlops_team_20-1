from pathlib import Path
from loguru import logger
import pandas as pd

from turkish_music_emotion.config import PROCESSED_DATA_DIR, RAW_DATA_DIR, INTERIM_DATA_DIR

class DataHandler:
    def __init__(self):
        self.data = None
        self.input_path = None

    def load_raw_data(self, input_path: Path = RAW_DATA_DIR / "Acoustic Features.csv"):
        self.input_path = input_path
        logger.info(f"Loading raw data from {self.input_path}")
        self.data = pd.read_csv(self.input_path)
        logger.success("Raw data loaded successfully.")
        return self.data

    def load_processed_data(self, input_path: Path):
        self.input_path = input_path
        logger.info(f"Loading processed data from {self.input_path}")
        self.data = pd.read_csv(self.input_path)
        logger.success("Processed data loaded successfully.")
        return self.data

    def load_interim_data(self, input_path: Path):
        self.input_path = input_path
        logger.info(f"Loading interim data from {self.input_path}")
        self.data = pd.read_csv(self.input_path)
        logger.success("Interim data loaded successfully.")
        return self.data

    def save_processed_data(self, filename: str):
        if self.data is None:
            logger.warning("No data to save. Load the data first.")
            return
        
        output_path = PROCESSED_DATA_DIR / filename
        logger.info(f"Saving processed data to {output_path}")
        self.data.to_csv(output_path, index=False)
        logger.success("Processed data saved successfully.")

    def save_interim_data(self, filename: str):
        if self.data is None:
            logger.warning("No data to save. Load the data first.")
            return
        
        output_path = INTERIM_DATA_DIR / filename
        logger.info(f"Saving interim data to {output_path}")
        self.data.to_csv(output_path, index=False)
        logger.success("Interim data saved successfully.")
