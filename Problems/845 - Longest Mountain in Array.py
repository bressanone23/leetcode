class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count = 0
        left = [arr[0]]
        right = []
        for x in arr[1:]:
            if right == []:
                if x > left[-1]:
                    left.append(x)
                elif x < left[-1]:
                    if len(left) > 1:
                        right.append(x)
                    else:
                        left = [x]
                else:
                    left = [x]

            else:
                if x < right[-1]:
                    right.append(x)
                elif x > right[-1]:
                    count = max(count, len(right)+len(left))
                    left = [right[-1],x]
                    right = []
                else:
                    count = max(count, len(right)+len(left))
                    left = [x]
                    right = []
            #print(left,right)
        return max(count, len(right)+len(left)) if len(right)!=0 else count
