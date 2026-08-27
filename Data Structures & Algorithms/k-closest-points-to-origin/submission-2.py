import math
class Solution:
    #using quicksort with the given points, we can sort the distances into an array and return k closest to origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Nieve solving: we sort the distances and just return k elements
        idx, idy = 0, 1
        distance_point_pairs = []
        for x, y in points:
            distance = self.getDistance(x, y)
            distance_point_pairs.append((distance, [x, y]))

        distance_point_pairs.sort()

        return [point for dist, point in distance_point_pairs[:k]]
    
    def getDistance(self, x1, y1) -> float:
        distance = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
        return distance


