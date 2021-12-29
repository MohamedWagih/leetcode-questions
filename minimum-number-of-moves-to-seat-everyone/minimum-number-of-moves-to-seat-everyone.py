class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum = 0
        for i in range(len(seats)):
            sum += abs(seats[i]-students[i])
        return sum