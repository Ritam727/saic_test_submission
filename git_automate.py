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
