#!/usr/bin/python
import time,sys,operator
#Definition for a point
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict_cache = {}
        self.dict_key2ts = {}
    # @return an integer
    def get(self, key):
        if key in self.dict_cache:
            #update LRU
            #self.dict_key2ts[key] = time.time()
            self.dict_key2ts[key] =  int(round(time.time() * 1000000))
            return self.dict_cache[key]
        else:
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.dict_cache) == self.capacity and key not in self.dict_cache: #need remove one based on LRU
            #remove
            sorted_cache = sorted(self.dict_key2ts.items(),key=operator.itemgetter(1))

            self.dict_cache.pop(sorted_cache[0][0])
            self.dict_key2ts.pop(sorted_cache[0][0])

        self.dict_cache[key] = value
        self.dict_key2ts[key] =  int(round(time.time() * 1000000))
        
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    lru = LRUCache(2)
    lru.set(1,'1')
    lru.set(2,'2')
    lru.set(3,'3')
#with keys : 2,3
    if lru.get(1) == -1 and lru.get(2) == '2' and lru.get(3) == '3':
        print 'pass 3 sets'
    else:
        print 'failed 3 sets test'
        sys.exit(0)
    #print lru.dict_cache
    #print lru.dict_key2ts
    lru.get(2)
    #print '..after get2 ts ...........'
    #print lru.dict_key2ts
    lru.set(4,'4')
    #print '..after set4 ts ...........'
    #print lru.dict_key2ts
#keys,2,4
    #print lru.dict_cache
    #print lru.dict_key2ts
    if lru.get(3) == -1 and lru.get(2) == '2' and lru.get(4) == '4':
        print 'pass get test'
    else:
        print 'faild to get test'
