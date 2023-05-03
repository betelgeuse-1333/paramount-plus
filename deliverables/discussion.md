**Overview**

I started this undertaking by treating it as I would any project that comes into a development 
team.  That means I created requirements, set scope, put together a spike to come up with
a plan, and then once that was in place I began coding.

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
_Unit Testing/Testing:_ If I am done early I will write some tests.\
_Indexes:_ The dat size means the database will be sufficiently performant.  As the 
datasets grow indexes may be needed, but they are out of scope for now.

**Users Stories:**  
Analyst/Dev:  The system needs to be able to be run locally on a developer's
or analyst's machine to validate.

**Requirements**
_Data Sets:_ There are three small data sets, but we should 
keep in mind a world where we 10GB or larger files.

_Time Frame:_  Assume that dev work should take 6 hours.  Design and scope assume that time is for hands-on keys
should last about 6 hours.  Incorporate long-term extensibility into the 
system wherever possible but do not prematurely optimize design such that it 
risks the time frame.

_Reporting:_  The system needs to support reporting that can aggregate on various aspects of the 
nested jsonl files and be able to self-reference/self-join.

**Risks:**\
_Feasibility:_  Low.  The project is straightforward.  Barring underlying\unforeseen
data issues the build is straightforward\
_Complexity:_  Low the data sets and joins are straightforward\
_Timing:_  High.  6 hours is a short time frame.

**Exploratory Data Analysis (EDA)**\
For this project, I felt EDA was important.  Before I started coding I wanted a sense 
of the data and how it all fits together, especially given that while it's not an uncommon
data set, it is new to me.

The thing that stood out was the jsonl files.  

In a perfect world, these are coming in as a stream and being processed 
with kaftka or spark streaming.  Here we were going to have to handle 
them a jsonl.  Moreover, the file sizes being discussed in a production 
realm meant I needed to at least consider their complexity in a 
world where there is also volume.

**Design:**\
I decided on setting up a Postgres database to house the data and spark as a data
engine to handle the back end.  Spark is a solid big-data solution that handles 
JSON files well and can handle streaming if it is ever needed.  Postgres is a familiar 
database system.  Both play well with Python.  Moreover psycopg2 and pyspark 
both are leveraged well within a Python system.  Spark can load directly to Postgres 
making that seamless.  Most of all I am familiar with both and given a 6-hour time 
constraint that was valuable as well.

I was tempted to try Trino.  Trino has become a trendy option because it handles
large volumes of data well, scales and can read directly from parquet.  If I had more
time to implement a spike to investigate it, I probably at least would have 
experimented with it.  In addition, the assignment specified a database and server,
and Trino is more akin to a query engine.

**A few conscious decisions I made:**\
-- I mix of OO and procedural approaches as is my style.  While not perfect I took some extra
time to adhere to DRY and encapsulation and separation of concerns principles.  While not
perfect, I tried to avoid being overly _quick and dirty_.\
-- With more time I would have cleaned up the module that processes the jsonl files, as I think it 
could have been broken up into a few more pieces.\
-- I spent a lot of time mulling the approach to processing the jsonl files.   The easy option 
was to use explode, but it was not computed efficiently even with a small data set.  I settled on 
a flat map approach that handles the data set one row at a time.  It runs much more quickly
and feels extensible to a larger data set.  The extra iterations did take time out of my 6 hours.


## **Discussion Questions**

Reading through the questions, there is an additional context that I wanted to use in answering them.
I made some assumptions:

### **ASSUMPTIONS:**
_User:_  System that is calling this as a service to access the data in Postgres.\
_Team Size:_ Small\
_Budget:_ Not a shoestring but we can't set money on fire burning through compute 
and other resources.\
_Platform/Tooling:_  There are no paramount systems or platforms 
(ie airflow as a service, etc) to serve to accelerate the work and reduce overhead.\
_Data Retention:_  I am assuming a few years.  IE the data being received is not thrown
away every 90 days.


**1: How you would approach this problem if each dataset was 100 GB instead of less than 
100 MB per dataset like in the assignment.  For each dataset type, how would you handle 
processing at this scale? How would your implementations change from this assignment? 
If you would choose different pipelines or tools, please discuss why you made those choices.**

**etl/elt**\
_comment_text/post_meta:_ For etl/elt I really do like spark.  It's perfectly suitable to
read in the parquet and .csv files as shown here.

_comment_info:_  The jsonl files make this slightly more complex.  My first step would be
to see if we can get access to the stream and process them on an ongoing basis.  Access and cost 
may be an issue in which case I think Spark continues to work fine.

I am not advocating for the use of SQL alchemy or an ORM here.  While those tools have their uses, volume and size do not increase the complexity.  I think a simple spark pipeline will scale nicely here.
The thing that obviously changes is local processing.  The use of a managed EMR cluster would be needed.

_database\storage:_  Obviously a local Postgres database makes it easy for a developer to spin up
but harder to scale.  I would create a time-boxed spike or test to look intp Trino as an option.  
Te ability to have a big snappy system that can power a web app and run off of parquet files is 
appealing.  If not Trino, then a managed service like aws rds would be my next choice.  Redshift gets 
expensive quickly and I think for what we are doing postgres on rds is sufficient.  If the data 
size gets larger and warrants it we can always migrate.  It's tempting because some of the data 
is unstructured to use NoSQL, but Spark is handling that upstream.

I don't _think_ any of my decisions would not scale to the sizes you are talking 
about (famous last words?).

**2: What about if you expected 10 GB of new data, for each source, daily, for the next year? 
For each dataset type, how would you handle processing at this scale? How would your 
implementations change this assignment? If you would choose different pipelines or tools than 
(1), please discuss why you made those choices.** 

**etl/elt**\
_comment_text/comment_info/post_meta:_ Interestingly this is less of an issue for etl than the statement above.  
We are dealing with less volume but with frequency.

_database\storage:_  10gb a day will add up quickly. This is where I will repeat my desire to try
try Trino.  Being able to get scalable performance off of a system leveraging parquet files will save a
ton of money on cloud costs.

**3: How would you go about deploying this solution to a production environment? Would you 
make any changes to the architecture outline above? Please discuss any anticipated methods 
for automating deployment, monitoring ongoing processes, ensuring the deployed solution is 
robust (as little downtime as possible), and technologies used.**

For production deployment there are a few more pieces we would need to talk about  A job database 
that tracks and logs all jobs including any errors is needed.   Monitoring with alerts around 
failure would be needed as well.  Given my assumptions above around a small team, I would want to
limit overhead.  That means leveraging AWS (or another cloud provider's) services.

ETL: Let's say we are processing this as batch.  I would recommend leveraging EMR for computing.
Use lambda to detect when a file hits s3 and make a call to an API endpoint that would kick 
off processing.  While lambda cannot handle the proposed job sizes, it is great as a monitoring
service.  It can send the file details to an API that would receive it and kick off a job.  We 
had a weekly etl job that was managed like this for a 500 GB file.  Using lambda to ping a job
API was easy.

Database:  Again I think Amazon RDS would be just fine as a managed database service if we
are going the Postgres route.  In addition, We would have to consider database migration.  Amazon 
DMS should be able to handle that for us.   If Trino is viable, then is just S3 with a hive 
meta store set up.

**Other:**\
-- Containers: Docker or Amazon's container service would also be leveraged here to ease deployment. 

-- Airflow:  One thing I have not proposed is airflow.  I really like airflow, especially for jobs that 
have complexity to them.  These transformations are simple though.  The additional overhead 
of maintaining an airflow server for a relatively simple etl process is unneeded.  AWS does have 
its Managed Workflow service, BUT it feels like additional overhead.  If airflow
already exists for other processes and can be leveraged as part of that pipeline.

--- Backups: Amazon Glacier to store the original data in case we need to rebuild our system would 
also be set up, with an automated retention policy/system.
