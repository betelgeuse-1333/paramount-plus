# **PARAMOUNT PLUS TECHNICAL EXERCISE**

This repo contains the software to create and build a post gres database to house comment data\
that is collected and transformed and loaded using spark.  The `requirements.txt` file
was constructed using `pip freeze > requirementstxt` and should list all dependencies.

**A few notes:**\
-- The software requires postgres 15 and the requisite driver/ jar file to run it.\
    --I have included the jar file in the repo\
-- For postgres you wil need to create a user and password (or use postgres) before you
can begin building it.\
-- The requirements.txt file has the details needed for all dependencies.\
-- Users will want to update the config file with any path and variable info 
specific to their environments.\
-- I highly recommend a venv.  I considered Docker, but I have had a handful of battles
with docker and ports and postgres so I kept it simple.\

**Running the software:**
_Building the database_\
1:  Run postgres_create_database.py from the command line at the root level once you
 have updated the config.py.\
    `python -m database.postgres_create_database.py`\
2:  Run postgres_create_tables.py from the command line at the root level\
    `python -m database.postgres_create_tables.py`\

_Loading the data to the tables:_\
1: Run post_meta_loader from the command line at the root level\
    `python -m data_loader.post_meta_loader.py`\
2: Run comment_text_loader from the command line at the root level\
    `python -m data_loader.comment_text_loader.py`\
3: Run comment_info_loader from the command line at the root level\
    `python -m data_loader.comment_info_loader.py`\

