from config import DbConfig
import utilities


# load post meta data
def load_post_meta_data():
    config_obj = DbConfig()
    spark = utilities.spark_sess()
    print(config_obj.post_meta)
    df = spark.read.parquet(config_obj.post_meta)

    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/"+config_obj.database+config_obj.environment) \
        .option("dbtable", config_obj.schema+".post_meta") \
        .option("user", config_obj.user) \
        .option("password", config_obj.password) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    return df


load_post_meta_data()