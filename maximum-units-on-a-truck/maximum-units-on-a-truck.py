class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ordered = sorted(boxTypes, key= lambda typ: typ[1], reverse=True)
        total_boxes=0
        units = 0
        for i in range(len(boxTypes)):
            if ordered[i][0] <= (truckSize - total_boxes):
                units += ordered[i][0] * ordered[i][1]
                total_boxes += ordered[i][0]
            else:
                units += (truckSize - total_boxes) * ordered[i][1]
                return units
        return units