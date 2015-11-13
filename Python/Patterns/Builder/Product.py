class Product(object):
    """description of class"""
    _parts = []

    def Add(self, part):
        self._parts.append(part)

    def Show(self):
        print("Product Parts -------")
        for part in self._parts:
            print(part)


