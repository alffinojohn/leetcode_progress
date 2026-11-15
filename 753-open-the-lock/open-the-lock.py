from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1

        q = deque([('0000', 0)])
        visited = {'0000'}

        while q:
                code,turn = q.popleft()
                if code == target:
                    return turn

                for i in range(4):
                    for direction in [-1,1]:
                        new_digit = (int(code[i]) + direction)  % 10
                        neighbour = code[:i] + str(new_digit) + code[i+1:]

                        if neighbour in dead or neighbour in visited:
                            continue

                        q.append((neighbour, turn+1))
                        visited.add(neighbour)


        return -1




        
        