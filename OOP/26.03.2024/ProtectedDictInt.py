from ProtectedDictIntIterator import ProtectedDictIntIterator
class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}
    def __setitem__(self, key, value):
        assert type(key) == int, "за умовою ключ має бути цілим"
        assert key not in self.__dict, "за умовою задачі, значення що уже є в словнику перевизначити не можна"
        self.__dict[key] = value
    def __delitem__(self, key):
        del self.__dict[key]

    def __getitem__(self, item):
        return self.__dict[item]
    def __str__(self):
        return f"ProtectedDectInt = {self.__dict}"
    def __contains__(self, item):
        return item in self.__dict
    def __len__(self):
        return len(self.__dict)
    def __add__(self, other):
        dictsum = ProtectedDictInt()
        for key in self.__dict:
            dictsum[key]=self.__dict[key]
        if type(other) == dict:
            for key in other:
                dictsum[key]=other[key]
        if type(other) == tuple or type(other)==list:
            assert len(other)%2==0, "непарна кількість символів в кортежі"
            for i in range(0, len(other), 2):
                dictsum[other[i]] = other[i+1]
        return dictsum
    def __sub__(self, other):
        dictsum = ProtectedDictInt()
        for key in self.__dict:
            if other!=key:
                dictsum[key] = self.__dict[key]
        return dictsum

    def __iter__(self):
        return ProtectedDictIntIterator(self)
    def keys(self):
        return self.__dict.keys()



if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "hello"
    # d[23] = "32"
    # d["Hello"] = "world"
    # print(d)
    # print(f"d[23]={ d[23]}")
    # print(25 in d)
    # print(len(d))
    d3 = (1, 2, 3, 4)
    print(d + d3)
    d4 = {1: 25, 4: 46}
    print(d + d4)
    print(d + d4 - 23)
    for el in d+d4:
        print(el)

