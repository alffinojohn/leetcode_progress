class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')', '{' : '}', '[': ']'
        }

        checking = []



        for brack in s:
            if brack in brackets:
                checking.append(brackets[brack])
            else:
                if checking != []:
                    close = checking.pop()
                    if close != brack:
                        return False
                else:
                    return False

        if checking:
            return False

        return True

                


        