

def binary_search(products, prefix, start):
    left, right = start, len(products)-1
    while left<=right:
        mid = left + (right-left)//2
        if products[mid] >=  prefix:
            right = mid  -1
        else:
            left = mid + 1
    
    return left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    
        products.sort()
        result = []
        n = len(products)
        match_start = 0
        prefix = ""
        for char in searchWord:
            prefix += char

            # match_start = bisect.bisect_left(products, prefix)
            match_start = binary_search(products, prefix, match_start)
            
            matches = []
            for product in products[match_start: match_start+3]:
                if product.startswith(prefix):
                    matches.append(product)
                
            result.append(matches)
        
        return result