class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0]*(n+1)
        for l,r,s in bookings:
            pref[l-1]+=s
            pref[r]-=s
        for i in range(1, n + 1):
            pref[i] += pref[i-1]
        return pref[:-1]