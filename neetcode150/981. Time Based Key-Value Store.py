class TimeMap:
    #logn, n

    def __init__(self):
        self.store= {} 
        #dict with key=string and val = list of list[val, tmstmp]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] #making sure key exists in dict 
        
        self.store[key].append([value, timestamp]) #assigning values to key

    def get(self, key: str, timestamp: int) -> str:
        res = "" #mpty string
        val = self.store.get(key, [])
        l, r = 0, len(val) - 1
        while l <= r:
            m = (l + r) // 2 #remeber: interger div (//)
            if val[m][1] <= timestamp: #valid val
                #remember <= rather than =
                res = val[m][0] #assign string val to result
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)