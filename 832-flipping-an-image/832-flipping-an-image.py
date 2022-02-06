class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i, j = 0, len(row)-1
            while i <= j:
                if row[i] == row[j]:
                    row[i] ^= 1;
                    row[j] = row[i]
                i += 1
                j -= 1
        return image