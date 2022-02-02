"""
Spark helpers
"""
from loguru import logger
from pyspark.sql import SparkSession


def get_spark_session() -> SparkSession:
    """
    Create a spark session
    :return: A spark session
    """
    logger.info("Getting the Spark Session.")
    return SparkSession.builder.getOrCreate()