from pygit2 import Repository


def curr_branch(branch='none'):
    if branch == 'none':
        branch = Repository('.').head.shorthand
    else:
        branch = branch
    print("The current branch is "+branch)

    return branch
