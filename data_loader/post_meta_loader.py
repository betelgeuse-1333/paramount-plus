#import psycopg2
from config import DbConfig
from database import database_connectors
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("load post_meta") \
    .config("spark.driver.extraClassPath", "/Users/David/Desktop/postgresql-42.6.0.jar") \
    .config("spark.executor.extraClassPath", "/Users/David/Desktop/postgresql-42.6.0.jar") \
    .getOrCreate()


config_obj = DbConfig()


# load post meta data
def load_post_meta_data(config_obj):
    df = spark.read.parquet(config_obj.post_meta)
    df.select("created_time",
              "post_h_id",
              "page_h_id",
              "name_h_id"
              )

    df.write\
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/paramountplus")\
        .option("dbtable", config_obj.schema+".post_meta")\
        .option("user", config_obj.user)\
        .option("password", config_obj.password)\
        .option("driver", "org.postgresql.Driver")\
        .mode("append")\
        .save()

    return df


load_post_meta_data(config_obj)

