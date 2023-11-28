class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next

    def set_prev(self, obj):
        self.__prev = obj

    def get_prev(self):
        return self.__prev


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if not self.head:
            self.head = obj
            self.tail = obj
            return

        prev = self.tail
        prev.set_next(obj)
        obj.set_prev(prev)
        self.tail = obj

    def remove_obj(self):
        if self.tail == self.head:
            self.tail = None
            self.head = None
            return

        self.tail = self.tail.get_prev()

    def get_data(self):
        obj = self.head
        lst = []
        while obj:
            lst.append(obj.get_data())
            obj = obj.get_next()
        return lst

