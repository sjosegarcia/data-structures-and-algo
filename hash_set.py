class HashSet:
    def __init__(self) -> None:
        self.size = 100
        self.hash_table = [[]] * self.size

    def add(self, key: int) -> None:
        _key = self._hash_key(key)
        self.hash_table[_key].append(key)

    def contains(self, key: int) -> bool:
        _key = self._hash_key(key)
        return key in self.hash_table[_key]
    
    def remove(self, key: int) -> None:
        _key = self._hash_key(key)
        if self.contains(key):
            self.hash_table[_key].remove(key)
    
    def _hash_key(self, key: int) -> int:
        return key % self.size