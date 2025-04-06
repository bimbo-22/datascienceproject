from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion.
    
    Attributes:
        source_url (str): URL of the source data.
        local_data_file (Path): Path to the local data file.
        unzip_dir (Path): Directory to unzip the data.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    """
    Configuration class for data validation.
    
    Attributes:
        root_dir (Path): Root directory for data validation.
        STATUS_FILE (Path): Path to the status file.
        unzip_data_dir (Path): Directory where the data is unzipped.
        all_schema (dict): Schema for data validation.
    """
    root_dir: Path
    STATUS_FILE: Path
    unzip_dir: Path
    all_schema: dict