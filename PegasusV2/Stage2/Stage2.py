import os
import sys
import xml.etree.ElementTree as xml
from urlparse import urlparse
from pyunpack import Archive
import random

class Stage2:
    def filterUnwantedSources(self, data_source_directory, data_destination_directory, required_file_names):
        walk = os.walk(data_source_directory)
        data_source_directories = [x[0] for x in walk]
        data_source_directories = data_source_directories[1:]

        for directory in data_source_directories:
            directory_walk = os.walk(directory)
            files = [x[2] for x in directory_walk][0]
            for source_file in files:
                if source_file not in required_file_names:
                    os.remove(directory + "//" + source_file)
                else:
                    #TODO: move the undeleted files to destination directory
                    pass

if __name__ == "__main__":
    stage2 = Stage2()
    args = sys.argv
    if len(args) > 1 and args[1] == 'ssd':
        stage2.filterUnwantedSources("D://BigData//Stage2_data//", "D://BigData//Stage2_data//", ["Posts.xml"])
    else:
        stage2.filterUnwantedSources("C://Users//PranayDev//Documents//BigData//ETL//Pegasus//Stage2//Stage2_data//", "C://Users//PranayDev//Documents//BigData//ETL//Pegasus//Stage2//Stage2_data//", ["Posts.xml"])