class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap():
    def __init__(self):
        self._capacity = 100
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def _hash(self, element):
        # return hash(element) % self._capacity
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        # print(index)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[index] = Entry(key, value)
                self._size += 1
                return None

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return True
                    # return "COVID-19 positive"
            else:
                return None

    # This function should remove the entry with specified key and return the value. In case if the key does not exist, None should be returned
    def remove(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    print(self._hashtable[i].value)
                    self._hashtable[i] = None
                    break
            else:
                return None

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break

        return self._hashtable[tmpInd].value


# Symtomps = HashMap()
#
# Symtomps.put("Bella", {"fullName": "Bella Brown",
#                        "birthMonth":"1",
#                        "birthDay":"1",
#                        "birthYear":"2001",
#                        "condition":"5"})
# Symtomps.put("Kate", {"fullName": "Kate John",
#                       "birthMonth": "5",
#                        "birthDay":"10",
#                        "birthYear":"2005",
#                        "condition":"0"})
# Symtomps.put("Sam", {"fullName": "Sam Strong",
#                      "birthMonth": "10",
#                        "birthDay":"11",
#                        "birthYear":"1970",
#                        "condition":"4"})
# Symtomps.put("Tim", {"fullName": "Tim Smith",
#                        "birthMonth":"7",
#                        "birthDay":"6",
#                        "birthYear":"1997",
#                        "condition":"1"})
# Symtomps.put("Lilly", {"fullName": "Lilly Williams",
#                        "birthMonth":"2",
#                        "birthDay":"3",
#                        "birthYear":"1988",
#                        "condition":"3"})
# Symtomps.put("COVID-19 negative", {"Healed": "yes"})
#
# r = "Kate"
# Symtomps.remove(r)
# h = Symtomps.hasKey("Bella")
# n="COVID-19 negative"
# p="Still COVID-19 positive:"
# print(n)
# print(h)
# print("\n")
# print(p)
# for elem in Symtomps:
#     print(elem.get("fullName"))
