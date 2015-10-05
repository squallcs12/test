import os
import random
import pdb
branchs = 10
commits = 20
for branch in range(branchs):
	os.system("git co master")
	branch_name = [random.choice(["do", "some", "thing", "new", "as", "client", "requirement"]) for x in range(6)]
	os.system("git co -b feature/%s-%s" % (branch, "-".join(branch_name)))
	for commit in range(commits):
		os.system("touch %s-%s" % (branch, commit))
		os.system("git add .")
		commit_name = " ".join([random.choice(["add", "new", "thing", "to", "current", "branch", "with", "code"]) for x in range(6)])
		os.system("git commit -m '[f] %s - %s\n\n%s'" % (branch, commit_name, " ".join(branch_name)))
