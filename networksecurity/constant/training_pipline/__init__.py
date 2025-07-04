import os
import sys
import numpy as np
import pandas as pd

"""
Common constand for training pipline
"""
TARGET_COLUMN = "Result"
PIPLINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str = "Artyifacts"
FILE_NAME:str = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"



"""
Data Ingestion related constant
"""

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str = "AbdulrhmanDataBase"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTRION_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2


"""
Data Validation related Constant
"""

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "valid"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"
DATA_VALIDATION_SCHEMA_FILE_NAME:str = "schema_validation.yaml"
SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")


"""
Data Validation relayed constant
"""

DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMATIONOBJ_FILE_NAME:str = "transformationObj.pkl"

DATA_TRANSFORMATION_IMPUTER_PARAMS:dict = {
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform"
}


