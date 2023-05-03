from pyspark.sql import SparkSession
from config import DbConfig


def spark_sess():
    config_obj = DbConfig()
    spark = SparkSession.builder \
        .appName("parse_data") \
        .config("spark.driver.extraClassPath", config_obj.postgres_driver_path) \
        .config("spark.executor.extraClassPath", config_obj.postgres_driver_path) \
        .getOrCreate()

    return spark
