import psycopg2
from config import DbConfig
from database import database_connectors

config_obj = DbConfig()


# Create tables
def create_post_meta_table(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    cur = conn.cursor()
    query = """
    CREATE TABLE """ + config_obj.schema + """.post_meta (
        created_time timestamp,
        post_h_id VARCHAR(50),
        page_h_id VARCHAR(50),
        name_h_id VARCHAR(50),
        PRIMARY KEY (created_time, post_h_id, page_h_id, name_h_id)
        );
        """
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

    return print("Table post_meta created")


def create_comment_text_table(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    cur = conn.cursor()
    query = """
    CREATE TABLE """ + config_obj.schema + """.comment_text (
    message TEXT,
        h_id VARCHAR(50),
        PRIMARY KEY (message, h_id)
        );
        """
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

    return print("Table comment_text created")


def create_comment_info_table(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    cur = conn.cursor()
    query = """
       CREATE TABLE """ + config_obj.schema + """.comment_info (
        h_id varchar(50),
        post_h_id VARCHAR(50),
        up_likes numeric(4),
        comment_count numeric(4),
        created_time timestamp,
        comment_h_id varchar(50),
        PRIMARY KEY (h_id, post_h_id, comment_h_id)
           );
           """
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

    return print("Table comment_info created")
