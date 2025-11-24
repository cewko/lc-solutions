import random


class RandomizedSet(object):
    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, value):
        boolean = value not in self.hashmap
        if boolean:
            self.hashmap[value] = len(self.array)
            self.array.append(value)
        return boolean
        
    def remove(self, value):
        boolean = value in self.hashmap
        if boolean:
            index = self.hashmap[value]
            last_value = self.array[-1]
            self.array[index] = last_value
            self.array.pop()
            self.hashmap[last_value] = index
            del self.hashmap[value]
        return boolean

    def getRandom(self):
        return random.choice(self.array)