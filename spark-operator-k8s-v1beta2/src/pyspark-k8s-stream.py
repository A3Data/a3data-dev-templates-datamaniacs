# import libraries
import time
from os.path import abspath
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession

# set default location for [spark-warehouse]
warehouse_location = abspath('spark-warehouse')

# main spark program
if __name__ == '__main__':

    # init spark session
    spark = SparkSession \
            .builder \
            .appName("pr-movies-analysis-stream") \
            .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1") \
            .config("spark.sql.warehouse.dir", warehouse_location) \
            .enableHiveSupport() \
            .getOrCreate()

    # set log level to info
    # [INFO] or [WARN] for more detailed logging info
    spark.sparkContext.setLogLevel("WARN")

    stream_movies_titles = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "a3dataedh-kafka-brokers.ingestion.svc.Cluster.local:9092") \
        .option("subscribe", "src-postgres-customers-json") \
        .option("startingOffsets", "latest") \
        .option("checkpoint", "checkpoint") \
        .load() \
        .select(from_json(col("value").cast("string"), sch_movies_titles, jsonOptions).alias("movies_titles"))
