class Solution:
    # O(n + nlogn) => O(nlogn)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos, speed] for pos, speed in zip(position, speed)]
        # O(nlogn)
        pairs.sort(reverse=True)
        
        # O(n)
        stack = []
        for pos, speed in pairs:
            arrival_time = (target-pos) / speed
            stack.append(arrival_time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)