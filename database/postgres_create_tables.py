import psycopg2
from config import DbConfig
from database import database_connectors

config_obj = DbConfig()


# Create tables
def create_post_meta_table(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    cur = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS """ + config_obj.schema + """.post_meta (
        created_time timestamp NULL,
        type VARCHAR(4) NULL,
        post_h_id VARCHAR(100) NULL,
        page_h_id VARCHAR(100) NULL,
        name_h_id VARCHAR(100) NULL
        );
        """
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

    return print("Table " + config_obj.schema + ".post_meta created")


create_post_meta_table()


def create_comment_text_table(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    cur = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS """ + config_obj.schema + """.comment_text (
    message TEXT NULL,
    h_id VARCHAR(50) NULL
        );
        """
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

    return print("Table " + config_obj.schema + ".comment_text created")


create_comment_text_table()


def create_comment_info_table(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    cur = conn.cursor()
    query = """
       CREATE TABLE IF NOT EXISTS """ + config_obj.schema + """.comment_info (
        h_id varchar(50) NULL, 
        post_h_id VARCHAR(50) NULL,
        comment_h_id VARCHAR(50) NULL,
        comment_count numeric(4) NULL,
        created_time timestamp NULL,
        up_likes numeric(4) NULL
           );
           """
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

    return print("Table " + config_obj.schema + ".comment_info created")


create_comment_info_table()
