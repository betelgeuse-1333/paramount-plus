from pygit2 import Repository
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


def curr_branch(branch='none'):
    if branch == 'none':
        branch = Repository('.').head.shorthand
    else:
        branch = branch

    print("The current branch is "+branch)

    return branch
