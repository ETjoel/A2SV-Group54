class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.timeToLive = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime-self.timeToLive
        if tokenId in self.tokens and self.tokens[tokenId] > limit:
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime-self.timeToLive
        ans = 0
        for key, value in self.tokens.items():
            ans += 1 if value > limit else 0
        return ans


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)