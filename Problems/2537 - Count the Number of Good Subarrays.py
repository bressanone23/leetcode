class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # res = cur = i = 0
        # count = Counter()
        # for j in range(len(A)):
        #     k -= count[A[j]]
        #     count[A[j]] += 1
        #     while k <= 0:
        #         count[A[i]] -= 1
        #         k += count[A[i]]
        #         i += 1
        #     res += i
        # return res

        dic = defaultdict(int)
        i=0
        count=res=0
        for j in range(len(nums)):
            # we simply count no. of pairs smartly , by incrementing frequency
            # after calculating count
            count+=dic[nums[j]]
            dic[nums[j]]+=1
            # if count exceeds or equlas to k, we start decrementing frequency from
            # ith index and decrementing all pairs formed using that index,
            # if it count stills greater then k, increment i and append in res
            # return res
            while count>=k:
                dic[nums[i]]-=1
                count-=dic[nums[i]]
                i+=1

            res+=i
            print(res)
        return res
