class Stats:
    def __init__(self, data: list):
        self.data = data
    def sum(self) -> float:
        return sum(self.data)
    def mean(self) -> float: # ค่าเฉลี่ย
        return sum(self.data) / len(self.data)
    def min(self) -> float:
        return min(self.data)
    def max(self) -> float:
        return max(self.data)
    
data = [10, 20, 30, 40, 50]
 
stats = Stats(data)

print(stats.sum())
print(stats.mean())
print(stats.min())
print(stats.max())
