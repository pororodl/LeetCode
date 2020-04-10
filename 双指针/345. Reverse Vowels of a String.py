class Solution:
    def reverseVowels(self, s: str) -> str:
        Len = len(s)
        l = 0
        r = Len-1
        vow = ['a','e','i','o','u','A','E','I','O','U']
        s_list = list(s)
        while l<r:
            while l<r and s_list[l] not in vow:
                l+=1
            while l<r and s_list[r] not in vow:
                r-=1
            if l<r:
                s_list[l],s_list[r] = s_list[r],s_list[l]
                l+=1
                r-=1
        return ''.join(s_list)

if __name__ == '__main__':
    sou = Solution()
    print(sou.reverseVowels('cade'))