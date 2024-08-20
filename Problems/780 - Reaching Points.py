class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # def dfs(tx,ty,memo):
        #     if (tx, ty) in memo:
        #         return memo[(tx, ty)]
        #     if tx < sx or ty < sy:
        #         return False
        #     if tx == sx and ty == sy:
        #         return True

        #     if dfs(tx-ty,ty,memo) or dfs(tx,ty-tx,memo):
        #         memo[(tx, ty)] = True
        #         return True

        #     memo[(tx, ty)] = False
        #     return False

        # return dfs(tx,ty,defaultdict(lambda: False))

        while True:
            if tx < sx or ty < sy:
                return False
            if tx == sx and ty == sy:
                return True
            else:
                if tx > ty:
                    if ty == sy:
                        return (tx-sx)%ty == 0
                    tx %= ty
                else:
                    if tx == sx:
                        return (ty-sy)%tx == 0
                    ty %= tx

            #print(tx,ty)
        return False
