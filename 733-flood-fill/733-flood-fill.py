from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_value = image[sr][sc]
        queue = deque([(sr,sc)])
        if start_value != newColor: 
            while queue:
                r, c = queue.popleft()
                image[r][c] = newColor
                for adj_r, adj_c in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                    if 0 <= adj_r < len(image) and 0 <= adj_c < len(image[0]) and image[adj_r][adj_c] == start_value:
                        queue.append((adj_r, adj_c))

        return image