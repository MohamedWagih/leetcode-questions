class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for edge in times:
            adj_list[edge[0]].append((edge[1], edge[2]))   

        elapsed_times = {node: float('inf') for node in range(1, n+1)}
        seen = [False] * (n+1)
        elapsed_times[k] = 0

        while True:
            cand_node = -1
            cand_elapsed = float('inf')
            for i in range(1, n+1):
                if not seen[i] and elapsed_times[i] < cand_elapsed:
                    cand_elapsed = elapsed_times[i]
                    cand_node = i
            if cand_node < 0: break
            seen[cand_node] = True
            for adj, elapsed in adj_list[cand_node]:
                elapsed_times[adj] = min(elapsed_times[adj], elapsed_times[cand_node] + elapsed)

        ans = max(elapsed_times.values())
        return ans if ans < float('inf') else -1