import psycopg2
from config import DbConfig

config_obj = DbConfig()


def admin_database_connection(config_obj=config_obj):
    conn = psycopg2.connect(
        host=config_obj.host,
        port=config_obj.port,
        user=config_obj.user,
        password=config_obj.password,
        database=config_obj.template_database
    )
    return conn


def paramount_database_connection(config_obj=config_obj):
    conn = psycopg2.connect(
        host=config_obj.host,
        port=config_obj.port,
        user=config_obj.user,
        password=config_obj.password,
        database=config_obj.database+config_obj.environment
    )
    return conn
