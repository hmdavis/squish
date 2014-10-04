import subprocess

COMMIT_MSG = "commit message"

REPO = subprocess.check_output(
	'echo $(git remote show -n origin | grep Push | cut -d : -f 2-3)',
	shell=True).strip()

BRANCH = subprocess.check_output(
	'echo $(git branch | grep \* | cut -d \* -f2)',
	shell=True).strip()

PWD = subprocess.check_output('pwd', shell=True).strip()

subprocess.call("mkdir ~/desktop/squishy", shell=True)
subprocess.call("mv * ~/desktop/squishy", shell=True)
subprocess.call("cd ..", shell=True)
subprocess.call("rm -r %s" % PWD, shell=True)
subprocess.call("git clone %s" % REPO, shell=True)
subprocess.call("cd %s" % PWD, shell=True)
subprocess.call("git checkout -b %s" % BRANCH, shell=True)
subprocess.call("mv ~/desktop/squishy/* .", shell=True)
subprocess.call("rm -r ~/desktop/squishy/", shell=True)
subprocess.call("git add . ", shell=True)
subprocess.call("git commit -m '%s'" % COMMIT_MSG, shell=True)
subprocess.call("git push origin master", shell=True)
