from config import DbConfig
import utilities


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


def process_jsons(spark):
    config_obj = DbConfig()
    df = spark.read.option("multiline", "true").json(config_obj.comment_info)
    rdd = df.rdd.flatMap(transform_row)
    df = rdd.toDF(["h_id", "post_h_id", "comment_h_id", "comment_count", "created_time", "up_likes"])

    return df


def comment_info_loader():
    spark = utilities.spark_sess()
    config_obj = DbConfig()
    df = process_jsons(spark)
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/"+config_obj.database+config_obj.environment) \
        .option("dbtable", config_obj.schema+".comment_info") \
        .option("user", config_obj.user) \
        .option("password", config_obj.password) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    return print("Data  loaded to the comment_info table")


comment_info_loader()

