from pygit2 import Repository
from pyspark.sql import SparkSession
import os


def spark_sess():
    spark = SparkSession.builder \
        .appName("load post_meta") \
        .config("spark.driver.extraClassPath", "/Users/David/Desktop/postgresql-42.6.0.jar") \
        .config("spark.executor.extraClassPath", "Users/David/Desktop//postgresql-42.6.0.jar") \
        .getOrCreate()

    return spark


def curr_branch(branch='none'):
    if branch == 'none':
        branch = Repository('.').head.shorthand
    else:
        branch = branch

    print("The current branch is "+branch)

    return branch
