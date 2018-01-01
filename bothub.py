#!/usr/bin/python3

import sys
from github import *

g = Github(client_id='',client_secret='')

if len(sys.argv) <= 1:
	exit("Usage: bothub.py <username>")
user = sys.argv[1]

repo_count = 0
fork_count = 0
status_count = [0,0,0,0]
status = ["identical","ahead","behind","diverged"]

try:
	repos = g.get_user(user).get_repos()

	for repo in repos:
		repo_count += 1
		# check if it's a source repo or a fork
		if repo.fork:
			fork_count += 1

			parent = repo.parent
			
			base = parent.owner.login+":"+parent.default_branch
			head = repo.owner.login+":"+repo.default_branch
			try:
				compare = repo.compare(base,head)
				line = "-{} -> Fork of {} = Status {}".format(repo.name,parent.full_name,compare.status)
				print(line)
				i = status.index(compare.status)
			except Exception as e:
				print(e)
				i = 3
			status_count[i] += 1

	report = "\nReport for user {}:".format(user)
	report += "\n- {} Repositories".format(repo_count)
	report += "\n- {} Forks ({:.3g}%)".format(fork_count,fork_count/repo_count*100)
	report += "\n- {} Identical Forks ({:.3g}% of all forks)".format(status_count[0],status_count[0]/fork_count*100)
	report += "\n- {} Ahead Forks ({:.3g}% of all forks)".format(status_count[1],status_count[1]/fork_count*100)
	report += "\n- {} Behind Forks ({:.3g}% of all forks)".format(status_count[2],status_count[2]/fork_count*100)
	report += "\n- {} Diverged Forks ({:.3g}% of all forks)".format(status_count[3],status_count[3]/fork_count*100)
	print(report)

except RateLimitExceededException as e:
	print(e)