from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import os

# get credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# set conf
conf = (
SparkConf()
    .set("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY_ID)
    .set("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
    .set("spark.hadoop.fs.s3a.fast.upload", True)
    .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .set("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore")
    .set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
)

# apply config
sc = SparkContext(conf=conf).getOrCreate()

if __name__ == '__main__':

    # Throws Exception if AWS credentials is not provided.
    if (AWS_ACCESS_KEY_ID is None) or (AWS_SECRET_ACCESS_KEY is None):
        raise Exception("AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY not found. You should provide that.")
    
    # init spark session
    spark = SparkSession\
            .builder\
            .appName("Delta - A3Data")\
            .getOrCreate()

    spark.sparkContext.setLogLevel("INFO")

    df = spark.read.format("json").load("s3a://a3data-architecture-team/landing-zone/kafka_events/src-postgres-customers-json/*/*/*/*/")
    
    # Get data on payload
    df = df.select("payload.*")

    # select columns for analysis
    cols = [
    'id',
    'sexo',
    'dt_update',
    'profissao',
    ]

    df = df.select(*cols)

    df_count_per_sex = df.groupby("sexo").count()
    df_count_per_sex.show()

    df.write.mode("overwrite").format("delta").save("s3a://a3data-architecture-team/delta/kafka_events/customers")

    spark.stop()