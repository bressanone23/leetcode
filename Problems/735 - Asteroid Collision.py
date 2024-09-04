class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        base = [A[0]]
        # for x in A[1:]:
        #     if x > 0:
        #         base.append(x)
        #     else:
        #         if not base:
        #             base.append(x)
        #             continue

        #         if base and base[-1] + x == 0:
        #             base.pop()
        #             continue

        #         if base and base[-1] < 0:
        #             base.append(x)
        #         elif base and base[-1] > 0:
        #             while base and base[-1] > 0 and (x + base[-1]) < 0:
        #                 base.pop()
        #             if base and base[-1] + x == 0:
        #                 base.pop()
        #                 continue
        #             if not base or (base and (base[-1] < 0)):
        #                 base.append(x)

        # return base


        for x in A[1:]:
            if base != [] and base[-1] > 0:
                if x > 0:
                    base.append(x)
                else:
                    if (x + base[-1]) == 0:
                        base.pop()
                    elif (x + base[-1]) < 0:
                        while (base != []) and base[-1] > 0 and (x + base[-1]) < 0:
                            base.pop()
                        if base != []:
                            if base[-1] + x == 0:
                                base.pop()
                                continue
                            if base[-1] < 0:
                                base.append(x)
                        else:
                            base.append(x)

            else:
                base.append(x)

        return base
