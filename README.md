# DownloadManagerMac
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  

## About the project

This is my first automation project using Python that also uses MacOS's built in Crontab VI editor to schedule when to
run the python script.

### What it does
This script creates folders in your downloads folder and places certain file types within those folders.
For example it will automatically create an `/Images` folder and place any files with the extension
of `'.png'` in that folder. You can set it to organize your downloads every minute, hour, daily, weekly, monthly, or whenever
using crontab.

## Getting started

### Prerequisites

This script can run on Windows but was designed for MacOS with use of the Crontab scheduler. I don't currently have support
for windows users.

### To clone
Use your computer's terminal and type the following:

```
$ git clone https://github.com/ikyle53/DownloadManagerMac.git
$ cd DownloadManagerMac
```
### 1. Install Python (if you don't have it)
Python can be installed [here](https://www.python.org/downloads/)!

### 2. Set up crontab
- Open your terminal and type `which python3` or `which python(version you use)` then press enter 
  - Copy the absolute path it gives you for later use
- Go into the cloned directory, right click the main.py file, then copy the absolute path from the properties for later use
- Within the terminal type `crontab -e`. This command allows you to edit crontab.
  - The terminal should have a bunch of `~` signs.
  - type `i` and hit enter. You'll now be in edit mode.
    - **Side note** before we set the schedule: crontab's scheduling format is unique.
    - It uses `* * * * *` as the format. The `*` represents any.
      - The first `*` is minutes, followed by hours, day of the month, the month, and finally day of the week.
      - To set it to daily you'd format it as `0 8 * * *`. This runs the code evertime the clock hits 8am.
  - Enter the following formats in order with spaces in-between: `<crontab schedule expression> <absolute path to python> <absolute path to main.py>`
  - It should look similar to the following `0 8 * * * /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/Kyle/Documents/DownloadManager/main.py`
- Once finished hit escape
- Type `:wb` to save and close crontab

That's it! I would recommend playing with the times and running the code in your IDE to see if the script is running correctly. If crontab isn't working
properly and executing the code it's probably due to having the wrong file path or you messed up the formatting.
  

## Credit
Jon McEwen's tutorial at [Medium](https://medium.com/geekculture/your-first-python-automation-project-6a7456b2d652)
