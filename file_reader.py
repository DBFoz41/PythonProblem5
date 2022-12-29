"""
File input class
"""

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.int_list = []
        self.str_split = ""
        
    def _file_read_all_str_list(self):
        f = open(self.file_name, "r")
        self.str_list = f.readlines()
        f.close()
        
    def file_as_int_list(self):
        self._file_read_all_str_list()
        self.int_list = []
        for str_num in self.str_list:
            self.str_split = str_num.split("\n")
            self.int_list.append(int(self.str_split[0]))
        return self.int_list
