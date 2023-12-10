class Solution:
    def totalMoney(self, n: int) -> int:
        def _sum(n):
            return (n / 2) *(1 + n)
        no_weeks = n // 7
        remaining_days = n % 7
        print(no_weeks, remaining_days)
        if no_weeks == 0:
            return int(_sum(n))
        elif no_weeks == 1:
            full_week = _sum(7) 
            remaining = _sum(remaining_days) + (no_weeks)*remaining_days
            print(full_week, remaining)
            return int(remaining+full_week)
        else:
            full_week = 0
            for i in range(no_weeks):
                full_week += _sum(7) + ((i) * 7)
                print(full_week)
            remaining = _sum(remaining_days) + (no_weeks)*remaining_days
            print(full_week, remaining)
            return int(remaining+full_week)

