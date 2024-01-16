class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = []
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        if val in self.RandomizedSet:
            return False
        
        self.RandomizedSet.append(val)
        self.hashMap[val] = len(self.RandomizedSet)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.RandomizedSet:
            return False

        indOfVal = self.hashMap[val]
        lastElement = self.RandomizedSet[-1]
        # swap the last item in positio indOfVal so that last value is safe and given value is removed
        self.RandomizedSet[indOfVal] = lastElement
        self.hashMap[lastElement] = indOfVal
        del self.hashMap[val]
        self.RandomizedSet.pop()

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.RandomizedSet)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()