# Task 4
I used subprocess, os and sys modules in python to make the script. It is a simple script that fetches from the upstream, checks whether there are changes with the remote branch with the current working tree, if there are changes to be made, it merges and outputs the changes. If there are merge conflicts, its up to the user to resolve them.

I made the script `git_automate.py` and put the following lines in it:
```python
import subprocess as sb
import sys, os

def main():
	remote, branch = "", ""
	if len(sys.argv[1:]) == 0:
		remote, branch = "upstream", "main"
	elif len(sys.argv[1:]) == 1:
		remote, branch = "upstream", sys.argv[1:][0]
	else:
		remote, branch = sys.argv[1:][0], sys.argv[1:][1]

	os.system("git fetch "+remote)
	changes = sb.run("git diff "+remote+"/"+branch+" .", shell = True, capture_output = True).stdout.decode("utf-8")
	print(changes)
	if changes != "":
		os.system("git merge "+remote+"/"+branch)
	else:
		print("Up to date")
main()
```

The script checks for any changes and outputs the changes to the console. If there are no changes, it simply outputs `Up to date`, otherwise, it merges the changes with the current working branch.

Usage:
1. `$ python git_automate.py`
    
    This compares and pulls changes from upstream/main.
2. `$ python git_automate.py [branch-name]`

    This compares and pulls changes from upstream/[branch-name].
3. `$ python git_automate.py [remote-name] [branch-name]`

    This compares and pulls changes from [remote-name]/[branch-name].

---
---

# What I learnt
Basic scripting and automating tasks with the help of python.

# Difficulties faced
Nothing as such

# Reference used
1. Google