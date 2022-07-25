# DJI-Flight-Logger
# github.com/temporal-driver/dji-flight-logger
import os
import configparser
import time
import data
from pathlib import Path

config = configparser.ConfigParser()
config.read('settings.ini')
working_dir = config['PATHS']['footage_dir']
files = []


def epoch_convert(sec):  # converts epoch seconds to YYYY/MM/DD
    filedate = time.strftime('%Y/%m/%d', time.gmtime(sec))
    return filedate


def read_files():
    for rf in os.listdir(working_dir):
        if rf.endswith('.MP4' or '.JPG'):
            f_name = os.path.basename(rf)
            f_path = os.path.join(working_dir, f_name)
            f_size = os.path.getsize(f_path)
            f_time = os.path.getmtime(f_path)
            f_date = epoch_convert(f_time)
            c_name = Path(f_path).stem
            locals()[c_name] = data.Footage(f_name, f_size,
                                            f_time, f_date, f_path)
            files.append(locals()[c_name])


def sort_by_time():
    sorted_files = sorted(files, key=lambda f: f.fileTime)
    return sorted_files


if __name__ == '__main__':
    read_files()
    for fd in files:
        print(fd.fileDate)

def count_dates():
    dates = []
    for d in files:
        dates.append(d.flightTime)