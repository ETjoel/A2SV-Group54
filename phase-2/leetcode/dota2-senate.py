class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque(senate)
        counter = Counter(senate)
        counter['R'] = counter['R']
        counter['D'] = counter['D']
        rmD, rmR = 0, 0
        while len(dq) > 1 and min(counter.values()) > 0:
            left = dq.popleft()
            if left == 'R' and not rmR:
                rmD+=1
                dq.append(left)
            elif left == 'R':
                rmR-=1
                counter[left]-=1
            elif left == 'D' and not rmD:
                rmR+=1
                dq.append(left)
            elif left == 'D':
                rmD-=1
                counter[left]-=1
            # print(dq)
        return 'Radiant' if dq[0] == 'R' else 'Dire'