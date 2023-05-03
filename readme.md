# **PARAMOUNT PLUS TECHNICAL EXERCISE**

This repo contains the software to create and build a post gres database to house comment data\
that is collected and transformed and loaded using spark.  The `requirements.txt` file
was constructed using `pip freeze > requirements.txt` and should list all dependencies.

**A few notes:**\
-- The software requires postgres 15 and the requisite driver/ jar file to run it.\
    --I have included the jar file in the repo\
-- You will need python 3.5 installed\
-- For postgres you wil need to create a user and password (or use postgres) before you
can begin building it.\
-- The requirements.txt file has the details needed for all dependencies.\
-- Users will want to update the config file.  Specifically:
*     - user: postgres username
*     - password: postgres password
-- I highly recommend a venv.  I considered Docker, but was concerned about time and complexity.

**Running the software:**\
The following commands should be executed in the terminal from the root level of the project, 
after activating your venv.\
`source /path/to/venv/paramount-plus/venv/bin/activate`

_Building the database_\
1:  Run postgres_create_database.py from the command line at the root level once you
 have updated the config.py.\
    `python -m database.postgres_create_database`\
2:  Run postgres_create_tables.py from the command line at the root level\
    `python -m database.postgres_create_tables`

_Loading the data to the tables:_\
1: Run post_meta_loader from the command line at the root level\
    `python -m data_loader.post_meta_loader`\
2: Run comment_text_loader from the command line at the root level\
    `python -m data_loader.comment_text_loader`\
3: Run comment_info_loader from the command line at the root level\
    `python -m data_loader.comment_info_loader`

