

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.storage = OrderedDict()
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.storage:
            return -1
        
        #to update that it was used
        self.storage.move_to_end(key)
        return self.storage[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.storage:
            self.storage.move_to_end(key)
            
        self.storage[key] = value
            
        if len(self.storage) > self.capacity:
                self.storage.popitem(last = False)
        
                

      
