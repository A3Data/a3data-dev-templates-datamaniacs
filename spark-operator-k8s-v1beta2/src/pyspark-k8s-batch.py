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
            .appName("Repartition Job")\
            .getOrCreate()

    spark.sparkContext.setLogLevel("INFO")

    df = spark.read.format("json").load("s3a://a3data-architecture-team/landing-zone/user/*.json")
    
    df.show()
    df.printSchema()

    df.write.mode("overwrite").format("parquet").save("s3a://a3data-architecture-team/processing-zone/user/")


    spark.stop()