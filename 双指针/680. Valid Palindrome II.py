class Solution:
    def validPalindrome(self, s: str) -> bool:
        Len = len(s)
        s_list = list(s)
        l = 0
        r = Len-1

        while l<r and s_list[l]==s_list[r]:
            l+=1
            r-=1
        if r-l>=2:
            print('l',l)

            return self.isPalindrome(s_list,l+1,r) or self.isPalindrome(s_list,l,r-1)
        return True

    def isPalindrome(self,s:list,l,r) ->bool:
        while l<r and s[l]==s[r]:
            l+=1
            r-=1

        if l>=r and l-r<=1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome('bcab'))