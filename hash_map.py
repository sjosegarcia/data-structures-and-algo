class HashMap:

    def __init__(self) -> None:
        self.size = 100
        self.hash_table = [[]] * self.size

    def _hash_key(self, key: int) -> int:
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        _key = self._hash_key(key)
        for index, collision in enumerate(self.hash_table[_key]):
            if collision[0] == key:
                self.hash_table[_key][index] = (key, value)
                return
        self.hash_table[_key].append((key, value))

    
    def get(self, key: int) -> int:
        _key = self._hash_key(key)
        for index, collision in enumerate(self.hash_table[_key]):
            if collision[0] == key:
                print(collision)
                return collision[1]
        return -1
    
    def remove(self, key: int) -> None:
        _key = self._hash_key(key)
        for index, collision in enumerate(self.hash_table[_key]):
            if collision[0] == key:
                self.hash_table[_key].pop(index)



#            print(f'key: {key} _key: {_key} index: {index} collision: {collision}')