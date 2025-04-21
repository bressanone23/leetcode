class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        #print(pos)
        count = 0

        for i, val in enumerate(nums):
            # Step 2: Check only within the same group (same number)
            for j in pos[val]:
                if (i * j) % k == 0:
                    count += 1
            # Step 3: Add current index to the list of indices for the number
            pos[val].append(i)

        return count
