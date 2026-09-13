class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.allTokens = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.allTokens[tokenId] = currentTime


    def renew(self, tokenId: str, currentTime: int) -> None:
        if (tokenId in self.allTokens) and (self.allTokens[tokenId] + self.time > currentTime):
            self.allTokens[tokenId] = currentTime
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, val in self.allTokens.items():
            if val + self.time > currentTime:
                count += 1

        return count



        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)