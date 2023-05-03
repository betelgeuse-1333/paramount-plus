from config import DbConfig
import utilities
from pyspark.sql.functions import encode


# load post meta data
def load_comment_text_data():
    config_obj = DbConfig()
    spark = utilities.spark_sess()
    df = spark.read.csv(config_obj.comment_text, header=True)
    df = df.withColumn("message", encode("message", 'utf-8'))

    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/"+config_obj.database+config_obj.environment) \
        .option("dbtable", config_obj.schema+".comment_text") \
        .option("user", config_obj.user) \
        .option("password", config_obj.password) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    return df


test = load_comment_text_data()
test.show(5)