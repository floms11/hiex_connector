class BaseType:
    def __getitem__(self, item):
        return self.values[item]

    def __getattr__(self, item):
        return self.values[item]
