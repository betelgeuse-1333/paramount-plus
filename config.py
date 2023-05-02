import utilities

branch = utilities.curr_branch()

if branch == "main":
    schema = "prod"
elif branch == "staging":
    schema = "qa"
else:
    schema = "development"

db_constants = {"host": "localhost",
                "port": 5432,
                "user": "maverick",
                "password": "g00se",
                "template_database": "template1",
                "schema": schema,
                "database": "paramountplus",
                "data_location": {"post_meta": "data/post_meta",
                                  "comment_text": "data/comment_text",
                                  "comment_info": "data/comment_info_jsonl"}}


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
        self.schema = self.config["schema"]
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.user = self.config["user"]
        self.password = self.config["password"]
        self.template_database = self.config["template_database"]
        self.database = self.config["database"]
