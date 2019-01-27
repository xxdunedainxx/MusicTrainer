from datetime import datetime
import os

"""
LOG LEVELS DEFINED 
    DEBUG: Information interesting for Developers, when trying to debug a problem.
    INFO: Information interesting for Support staff trying to figure out the context of a given error
    WARN to FATAL: Problems and Errors depending on level of damage.
"""



class LogFactory():

    def __init__(self,file, log_level="ALL"):

        # file path
        self._file_path=file
        self._log_level=log_level

        # create log directory if it does not exist
        if self._dir_exists() == False:
            self._create_log_direrctory()

        # Establish file stream
        self.establish_file_stream()

    def establish_file_stream(self):
        self._file_stream=open(self._file_path,'a')

    def dispose_stream(self):
        if self._file_stream.closed is False:
            self._file_stream.close()

    def _create_log_direrctory(self,f=None):
        if f is None:
            os.mkdir(self._parse_directory_from_file(self._file_path))
        else:
            os.mkdir(self._parse_directory_from_file(f))

    def _parse_directory_from_file(self,file):
        # Probs a better way to do this lol
        t=file.split("\\")
        t=t[:(len(t) - 1)]

        directory=""
        for d in t:
            directory+=f"{d}\\"

        return directory

    def _dir_exists(self):
        if os.path.isdir(self._parse_directory_from_file(self._file_path)):
            return True
        else:
            return False
    def commit_data(self):
        self._file_stream.flush()

    def write_log(self,data,level="INFO"):
        # If the level is enabled to to cached
        if LogFactory.LOG_LEVELS(level,self._log_level):
            self._file_stream.write(f"[{level}: {str(datetime.now())}] {data}\n")

    @staticmethod
    def LOG_LEVELS(level,logger_level):
        levels={
            'DEBUG' : ['DEBUG','WARN','ERROR'],
            'INFO' : ['INFO'],
            'TRACE' : ['WARN','ERROR'],
            'ALL' : ['DEBUG','WARN','ERROR','INFO']
        }

        if level in levels[logger_level]:
            return True
        else:
            return False


