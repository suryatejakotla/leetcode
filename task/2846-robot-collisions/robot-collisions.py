from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = []
        
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]
                    if healths[i] < healths[j]:
                        healths[j] -= 1
                        healths[i] = 0
                    elif healths[i] > healths[j]:
                        healths[i] -= 1
                        healths[j] = 0
                        stack.pop()
                    else:
                        healths[i] = healths[j] = 0
                        stack.pop()
                        break
        
        return [h for h in healths if h > 0]