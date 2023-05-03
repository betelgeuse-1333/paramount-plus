import utilities
from pathlib import Path

branch = utilities.curr_branch()

if branch == "main":
    environment = "_prod"
elif branch == "staging":
    environment = "_qa"
else:
    environment = "_development"

db_constants = {"host": "localhost",
                "port": 5432,
                "user": "",
                "password": "",
                "template_database": "template1",
                "environment": environment,
                "database": "paramountplus",
                "schema": "commentdata",
<<<<<<< HEAD
                "postgres_driver_path": "postgresql-42.3.0.jar",
=======
                "postgres_driver_path": "/path/toyour/jar-file/postgresql-42.3.0.jar",
>>>>>>> 2d320caae74787befb3f3c242e7aca0fc384b0d0
                "data_location": {"post_meta": str(Path('data_loader', 'data', 'post_meta')),
                                  "comment_text": str(Path('data_loader', 'data', 'comment_text')),
                                  "comment_info": str(Path('data_loader', 'data', 'comment_info_jsonl'))}}


class DbConfig:
    def __init__(self, config={}):

        if not config:
            self.config = db_constants
        else:
            self.config = config

        self.data_location = self.config["data_location"]
        self.post_meta = self.data_location["post_meta"]
        self.comment_text = self.data_location["comment_text"]
        self.comment_info = self.data_location["comment_info"]
        self.environment = self.config["environment"]
        self.schema = self.config["schema"]
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.user = self.config["user"]
        self.password = self.config["password"]
        self.template_database = self.config["template_database"]
        self.database = self.config["database"]
        self.postgres_driver_path = self.config["postgres_driver_path"]

