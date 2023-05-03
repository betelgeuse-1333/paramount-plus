from pyspark.sql import SparkSession
from config import DbConfig
import utilities
from pyspark.sql.functions import col, explode


def transform_row(row):
    h_id = row["h_id"]
    posts = row["posts"]["data"]
    transformed_posts = []
    for post in posts:
        post_h_id = post["h_id"]
        if "comments" in post:
            comments = post["comments"]["data"]
            for comment in comments:
                comment_h_id = comment["h_id"]
                comment_count = comment["comment_count"]
                created_time = comment["created_time"]
                up_likes = comment["up_likes"]
                transformed_posts.append((h_id, post_h_id, comment_h_id, comment_count, created_time, up_likes))
        else:
            transformed_posts.append((h_id, post_h_id, None, None, None, None))
    return transformed_posts


def process_jsons():
    config_obj = DbConfig()
    spark = utilities.spark_sess()
    df = spark.read.option("multiline", "true").json(config_obj.comment_info)
    rdd = df.rdd.flatMap(transform_row)
    df = rdd.toDF(["h_id", "post_h_id", "comment_h_id", "comment_count", "created_time", "up_likes"])

    return df

test = process_jsons()
test.show(100)

