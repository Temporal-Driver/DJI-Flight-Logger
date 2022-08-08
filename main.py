import os
import configparser
import sys
import time
import data
from pathlib import Path

config = configparser.ConfigParser()
config.read('settings.ini')
footage_dir = config['PATHS']['footage_directory']


def main():
    check_dir()
    files = read_files()
    for f in files:
        print(f.fileName)


def check_files():
    logfile = open(os.getcwd() + "\\filelog.txt")


def read_files():
    presorted_files = []
    for rf in os.listdir(footage_dir):
        if rf.endswith('.MP4' or '.JPG'):
            f_name = os.path.basename(rf)
            f_path = os.path.join(footage_dir, f_name)
            f_size = os.path.getsize(f_path)
            f_time = os.path.getmtime(f_path)
            f_date = time.strftime('%Y/%m/%d', time.gmtime(f_time))
            c_name = Path(f_path).stem
            locals()[c_name] = data.Footage(f_name, f_size,
                                            f_time, f_date, f_path)
            presorted_files.append(locals()[c_name])
    files = sorted(presorted_files, key=lambda f: f.fileTime)
    return files


def check_dir():  # Checks if the directory in settings.ini exists, then checks if there's footage.
    if os.path.isdir(footage_dir):
        footage = 0
        for f in os.listdir(footage_dir):
            if f.endswith('.MP4' or '.JPG'):
                footage += 1
        if footage > 0:
            return
    else:
        print("Directory path invalid or no footage was found. Please check 'settings.ini' and try again.")
        input("Press enter to exit;")
        sys.exit()


if __name__ == '__main__':
    main()
