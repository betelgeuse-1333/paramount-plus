from pyspark.sql import SparkSession
from config import DbConfig
import utilities
from pyspark.sql.functions import col, explode


def data_go_boom(df, column, alias):
    df = df.withColumn(alias, explode(col(column)))
    return df


# load post meta data
def load_comment_info_data():
    config_obj = DbConfig()
    spark = utilities.spark_sess()
    df = spark.read.option("multiline", "true").json(config_obj.comment_info)
    df = data_go_boom(df, 'posts.data', 'post')
    df = df.select(col('h_id'),
                   col("post"),
                   col('post.h_id').alias('post_id'),
                   col('post.comments.data').alias("comments_data"))
    print(df.count())
    df.write.parquet("data/temp/coment_info")
    df = data_go_boom(df, 'comments_data', 'comments_stats')
    df = df.select(col("h_id"),
                   col("post"),
                   col("post_id"),
                   col("comments_data"),
                   col("comments_stats"),
                   col("comments_stats.up_likes"))


    #df = df.select(col('h_id'),
    #               col("posts"),
    #               col('posts.h_id').alias('post_h_id'),
    #               col('posts.comments'),
    #               col('posts.comments.data').alias("comments_data"))

#    df.write \
#        .format("jdbc") \
#        .option("url", "jdbc:postgresql://localhost:5432/"+config_obj.database+config_obj.environment) \
#        .option("dbtable", config_obj.schema+".comment_text") \
#        .option("user", config_obj.user) \
#        .option("password", config_obj.password) \
#        .option("driver", "org.postgresql.Driver") \
#        .mode("append") \
#        .save()

    return df


#test = load_comment_info_data()
#test.show(5)

spark = utilities.spark_sess()
test = spark.read.parquet("data/temp/coment_info")
print(test.count())
test.show(100)
test1 = data_go_boom(test, 'comments_data', 'comments_stats')
print(test1.count())
test1.show(100)
#test2 = test1.select(col("h_id"),
#                     col("post"),
#                     col("post_id"),
#                     col("comments_data"),
#                     col("comments_stats"),
#                     col("comments_stats.up_likes"),
#                     col("comments_stats.comment_count"),
#                     col("comments_stats.created_time"),
#                     col("comments_stats.h_id").alias("commenter_hid"))

#print(test2.count())

