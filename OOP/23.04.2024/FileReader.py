from abc import ABCMeta, abstractmethod


class FileReaderObserver(metaclass=ABCMeta):
    @abstractmethod
    def onReceive(self, line):
        pass

class FileReader():
    def __init__(self, file_name):
        self.file_name = file_name
        self.observers = []
    def subscribe(self, observer):
        self.observers.append(observer)
    def read(self):
        with open(self.file_name) as f:
            for line in f:
                for observer in self.observers:
                    observer.onReceive(line.rstrip())

if __name__ == '__main__':
    fr = FileReader("input.txt")
    fr.read()