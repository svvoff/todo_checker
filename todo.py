#!/usr/local/bin/python3

from git import Repo
from git import diff
import re
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--print-diff', '-d', default=False, action='store_true')
parser.add_argument('--path', '-p')
parser.add_argument('--from-branch', help='parent branch name')
parser.add_argument('--search', '-s', default='TODO:', help='looking for item, \'TODO:\' by default')

args = parser.parse_args()
print_diff = args.print_diff
item = args.search

#if not item:
#    item = 'TODO:'

path = args.path

repo = Repo(path)

from_branch_name = args.from_branch

diff_branches = from_branch_name + '...' + repo.active_branch.name
d = repo.git.diff(diff_branches)

if print_diff:
	print("\n##########################################")
	print(d)
	print("##########################################\n")

diff_branches

print('Search ' + item + ' in diff for ' + diff_branches)

print('Number of \'' + item+ '\': ' + str(d.count(item)))
