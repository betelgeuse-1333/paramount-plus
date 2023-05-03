import psycopg2
from config import DbConfig
from database import database_connectors

config_obj = DbConfig()


# Create the database
def create_database(config_obj=config_obj):
    conn = database_connectors.admin_database_connection(config_obj)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE DATABASE  "+config_obj.database+config_obj.environment+" ENCODING 'UTF8';")
    cur.close()
    conn.commit()
    conn.close()

    return print("Database: "+config_obj.database+config_obj.environment+" created")


create_database()


def create_schema(config_obj=config_obj):
    conn = database_connectors.paramount_database_connection(config_obj)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS "+config_obj.schema+";")
    cur.close()
    conn.commit()
    conn.close()

    return print("Database Schema: "+config_obj.schema+" created")


create_schema()