# iTunes Connect Autodownload

ITC Autodownload automatically downloads the latest sales reports from iTunes Connect. Since such reports are only preserved by Apple for 30 days, it is important to continuously fetch these reports to preserve historical sales statistics.

## Requirements

* Python 2.7
    * Probably Python 2.6 works as well.

## Installation

* Download this repository.
* Create a file called `autoingestion.properties` with your iTunes Connect credentials. This file should be in the format:

```
userID = <USERNAME>
password = <PASSWORD>
```

* Open `autodownload.py` in the text editor and edit the `vendorid = ########` line with your iTunes Connect vendor ID.
    * This is an 8-digit number displayed at the top of the Sales and Trends page in the iTunes Connect web interface.
* Optionally install the [notifymail] dependency if you plan to use the trampoline script:

```
$ pip install notifymail
```

## Usage

To download the latest sales reports:

```
$ python autodownload.py
```

To download the latest sales reports and report errors via [notifymail]:

```
$ python autodownload_trampoline.py
```

[notifymail]: https://github.com/davidfstr/notifymail

## License

This code is provided under the MIT License.

## History

This script was originally created in August 2011 when I published my first apps on the iOS App Store. As of 2014 I am using it to track apps on the Mac App Store, notably [Burn Planner].

This is some of the earliest Python code I wrote, so it is not fully [PEP 8] compliant.

[Burn Planner]: http://dafoster.net/projects/burn-planner/
[PEP 8]: http://www.python.org/dev/peps/pep-0008/