from pyspark import SparkContext
from pyspark.sql import SQLContext
from pygit2 import Repository

sc = SparkContext.getOrCreate()
spark = SQLContext(sc)


def curr_branch(branch='none'):
    if branch == 'none':
        branch = Repository('.').head.shorthand
    else:
        branch = branch

    print("The current branch is "+branch)

    return branch