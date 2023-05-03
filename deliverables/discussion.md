**Overview**

I started this undertaking by treating it as I would any project that comes in to a development 
team.  That means I created requirements, set scope, put together a spike to come up with
a plan and then once that was in place I began coding.

**Steps:**\
Requirements Gathering\
EDA\
Design\approach\
Build


**Requirements Info:**\
Project Overview\
We have a sample data set of chat and sentiment data that we want to load 
and evaluate.


**In Scope:**\
A database server and database housing the sample data and sample 
queries designed to answer basic questions.

**Not In Scope:** \
_Managed Cloud Service:_ To make it easy for individuals to run it should be able 
to be run locally.\
_Big Data:_  Long term this project will be used to handle much larger data 
sets.  The system should be designed with extensibility in mind, 
but avoid premature optimization that would jeopardize timing.\
_Endpoints/Access:_ Out of scope are endpoints and other pieces of software
designed to provide access to the database.\
_Database Migration:_  Again for this exercise this is out of scope.\
_Unit Testing/Testing:_ If I am done arly I will write some tests.

**Users Stories:**  
Abalyst/Dev:  The system needs to be able to be run locally on a developer's
or analyst's machine to validate.

**Requirements**
_Data Sets:_ There are three small data sets, but we should 
keep in mind a world where we 10gb or larger files.

_Time Frame:_  Assume that dev work should take 6 hours.  Design and scope assumes that hands on keys
should last about 6 hours.  Incorporate long term extensibility into the 
system wherever possible but do not prematurely optimize design such that it 
risks the time frame.

**Risks:**\
_Feasibility:_  Low.  The project is straightforward.  Barring underlying\unforeseen
data issues the build is straightforward\
_Complexity:_  Low the data sets and joins are straightforward
_Timing:_  High.  6 hours is a short time frame.

**Exploratory Data Analysis (EDA)**\
For this project I felt EDA was important.  Before I started coding I wanted a sense 
of the data and how it all fit together, esp given that while its not an uncommon
data set, it is new to me.

The thing that stood out was the jsonl files.  

In a perfect world these are coming in as a stream and being processed 
with kaftka or spark streaming.  Here we were going to have to handle 
them a jsonl.  Moreover, the file sizes being discussed in a production 
realm meant I needed to at least consider their complexity in a 
world where there is also volume.

**Design:**\
I decided on setting up a postgres database to house the data and spark as a data
engine to handle the back end.  Spark is a solid a big data solution that handles 
json files well, and can handle streaming if it is ever needed.  Postgres is a fmiliar 
database system.  Both play well with python.  Mor over between psycopg2 and pyspark 
both are leveraged well within a python system.  Spark can load directly to postgres 
making that seamless.  Most of all I am familiar with both and given a 6 hour time 
constraint that was valuable as well.

I was tempted to try Trino.  Trino has become a trendy option because it handles
large volumes of data well, scales and can reqd directly from parquet.  If I had more
timme to implement a spike to investigate it, I probably at least would have 
experimented with it.  In addition, the assignment specified a data base and server,
and Trino is more akin to a query engine.

The rest of this repo contains the build piece.

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

At this point the data should be loaded to postgres.  A few decisions I am hoping you 
take note of.  I put in extra time to build out a codebase tha tadheres to principles
of engineering like DRY, separation of concerns and encapsulating what changes.  I used
a mix of OO and procedural.  With more time I would have cleaned up the module that
processes the jsonl files.  

I spent alot of time on that piece trying different approaches allowing it to take 
up a big chunk of time.  The easy option was to use explode, but it was not
compute efficient even with a small data set.  I settled on a flat map approach that handles 
the data set one row at a time.  Its runs much more quickly and feels like it would be 
extensible to a larger data set.  The extra time prevented me from cleaning the functions 
up, as I think it could have been broken up into a few more pieces.


Discussion Questions