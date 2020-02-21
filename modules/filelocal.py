import csv

__slots__ = ['atCSV', 'atTXTlines', 'atError']

class Filelocal:
    def openFileCsv(self, filename, mode):
        try:
            data_file = open(filename, mode)
            data_file_return = csv.DictReader(data_file)
            self.atCSV = data_file
        except IOError as e:
            self.atError = "Unable to open the file", filename, "Error: ", e
        else:
            return data_file_return

    def openFileTxt(self, filename, mode):
        try:
            data_file_return = open(filename, mode)
            self.atTXTlines = data_file_return.readlines()
        except IOError as e:
            self.atError = "Unable to open the file", filename, "Error: ", e
        else:
            return data_file_return

    def save_result(self, filename):
        pass
