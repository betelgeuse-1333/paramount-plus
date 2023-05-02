import os
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("load post_meta") \
    .config("spark.driver.extraClassPath", "/Users/David/Desktop/postgresql-42.6.0.jar") \
    .config("spark.executor.extraClassPath", "Users/David/Desktop//postgresql-42.6.0.jar") \
    .getOrCreate()

df = spark.read.parquet("/Users/David/Documents/repos/paramountplus/data_loader/data/post_meta")


df.printSchema()

df.write\
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/paramountplus")\
    .option("dbtable", "development.post_meta")\
    .option("user", "maverick")\
    .option("password", "g00se") \
    .option("driver", "org.postgresql.Driver")\
    .mode("overwrite")\
    .save()

