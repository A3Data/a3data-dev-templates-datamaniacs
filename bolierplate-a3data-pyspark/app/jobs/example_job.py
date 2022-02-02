"""
Simple Demo pipeline logic
"""
from app.helpers.spark import get_spark_session
from loguru import logger
from pyspark.sql import (
    SparkSession, 
    DataFrame
)

def create_test_data(spark: SparkSession) -> DataFrame:
    """Create Dataframe with 100 lines"""
    return spark.range(1,100)

def run() -> None:
    """Main ETL script definition."""
    spark = get_spark_session()

    logger.info("Creating and showing data in ETL")
    df = create_test_data(spark)
    
    return df.show()