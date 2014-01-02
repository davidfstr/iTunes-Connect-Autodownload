import os
import re
import datetime
import subprocess
import keychain

# Lookup credentials from the login keychain
credentials = keychain.Keychain().get_generic_password('login', servicename='ITC_Autodownload_Script__iTunes_Connect')
email = credentials['account']
password = credentials['password']
vendorid = 85050101

# Find all reports in the current directory
reports = []                                                # list of (vendorid, YYYYMMDD), both strings
for filename in os.listdir('.'):
    # NOTE: Download filename format changed on 2011-11-03
    m = re.match(r'S_D_([0-9]+)_([0-9]{8})(_[^.]*)?\.txt(\.gz)?', filename)
    if m is None:
        continue
    reports.append((m.group(1), m.group(2)))
if len(reports) == 0:
    exit('No reports found in the current directory.')

# Find all report dates for the vendor of interest
dates = [x[1] for x in reports if x[0] == str(vendorid)]    # list of YYYYMMDD
if len(reports) == 0:
    exit('No reports in the current directory match the vendor ID ' + str(vendorID) + '.')

# Determine reports available for download
downloadableDates = []                                      # list of YYYYMMDD
now = datetime.datetime.now()
for i in xrange(14):
    downloadableDates.append((now - datetime.timedelta(days = i+1)).strftime('%Y%m%d'))

# Determine reports available for download that haven't already been downloaded
missingDates = list(set(downloadableDates) - set(dates))    # list of YYYYMMDD
missingDates.sort()
if len(missingDates) == 0:
    print 'All reports have been downloaded already.'
    exit(0)

# Download all missing reports, recording any errors
downloadErrors = []                                         # list of (YYYYMMDD, stdoutdata, stderrdata)
for curDate in missingDates:
    downloader = subprocess.Popen(['java', 'Autoingestion', email, password, str(vendorid), 'Sales', 'Daily', 'Summary', curDate], stdout=subprocess.PIPE)
    out, err = downloader.communicate()
    if 'File Downloaded Successfully' not in out:
        downloadErrors.append((curDate, out, err))

# Print summary
if len(downloadErrors) == 0:
    print "Downloaded %s report(s)." % (len(missingDates))
else:
    for (date, out, err) in downloadErrors:
        print date + ':'
        print out
        print
    print "Error downloading %s report(s). Remaining %s reports downloaded." % (len(downloadErrors), len(missingDates) - len(downloadErrors))
    exit(1)
