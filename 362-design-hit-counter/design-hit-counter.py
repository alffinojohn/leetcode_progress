class HitCounter:

    def __init__(self):
        self.counter = {}
        

    def hit(self, timestamp: int) -> None:
        self.counter[timestamp] = self.counter.get(timestamp, 0) + 1


        

    def getHits(self, timestamp: int) -> int:
        start = max(1, timestamp-299)
        total = 0

        for second in range(start, timestamp+1):
            total += self.counter.get(second, 0)

        return total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)