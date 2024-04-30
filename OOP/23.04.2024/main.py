from FileReader import FileReaderObserver, FileReader


class ShowLines(FileReaderObserver):
    def onReceive(self, line):
        print(line)
class WordExist(FileReaderObserver):
    def __init__(self, word):
        self.word = word
        self.true = False

    def onReceive(self, line):
        if self.word in line:
            self.true = True

class WordNumber(FileReaderObserver):
    def __init__(self):
        self.number = 0
    def onReceive(self, line):
        words = line.split()
        self.number += len(words)

class Different(FileReaderObserver):
    def __init__(self):
        self.difer = set()
    def onReceive(self, line):
        line = line.lower()
        words = line.split()
        words = set(words)
        self.difer = self.difer.union(words)




if __name__ == '__main__':
    showLines = ShowLines()
    word = WordExist("main")
    number = WordNumber()
    dif = Different()
    fr = FileReader("input.txt")
    fr.subscribe(showLines)
    fr.subscribe(word)
    fr.subscribe(number)
    fr.subscribe(dif)
    fr.read()
    print(word.true)
    print(number.number)
    print(len(dif.difer))

