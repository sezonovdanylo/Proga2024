class ProtectedDictInt01(dict):
    def __setitem__(self, key, value):
        assert type(key) == int, "за умовою ключ має бути цілим"
        assert key not in self, "за умовою задачі, значення що уже є в словнику перевизначити не можна"
        super().__setitem__(key, value)


if __name__ == '__main__':
    d = ProtectedDictInt01()
    d[23] = "hello"
    d[23] = "32"
    d["Hello"] = "world"
    print(d)