#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import subprocess
import notifymail
import sys

# Run script
python = sys.executable
scriptDir = sys.path[0]
script = subprocess.Popen([python, 'autodownload.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=scriptDir)
out, err = script.communicate()
output = out + err

# Display output
print output,

# If error, then send a notification email
if script.returncode != 0:
    notifymail.send('[ITC Autodownload] Error', output)