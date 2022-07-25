# DJI-Flight-Logger Classes
# I'm sure there's a smarter way to do this but I sure haven't found it
class Footage:
    def __init__(self, file_name, file_size, file_time, file_date, file_path):
        self.fileName = file_name
        self.fileSize = file_size
        self.fileTime = file_time
        self.fileDate = file_date
        self.filePath = file_path


class Flight:
    def __init__(self, flight_date, first_file, last_file):
        self.flightDate = flight_date
        self.firstFile = first_file
        self.lastFile = last_file