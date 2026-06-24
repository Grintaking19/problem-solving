from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.ds[key]
        l, r = 0, len(array)  - 1
        res = ("", 0)
        while l <= r:
            mid = l + (r - l) // 2
            if array[mid][1] == timestamp:
                return array[mid][0]
            elif array[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = array[mid]
                
        return res[0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)