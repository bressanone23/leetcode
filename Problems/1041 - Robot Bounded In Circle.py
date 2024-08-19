class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial = [0,0]
        direction = 1

        for _ in range(4):
            for x in instructions:
                if x == 'G':
                    if direction == 1:
                        initial[1] += 1
                    elif direction == 2:
                        initial[0] += 1
                    elif direction == 3:
                        initial[1] -= 1
                    else:
                        initial[0] -= 1
                elif x == 'L':
                    if direction != 1:
                        direction -= 1
                    else:
                        direction += 3
                else:
                    if direction != 4:
                        direction += 1
                    else:
                        direction -= 3

        return initial == [0,0]


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        dx, dy, x, y = 0, 1, 0, 0
        for l in 4*instructions:
            if l == "G":
                x, y = x+dx, y+dy
            elif l == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x,y) == (0,0)
