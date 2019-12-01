class Solution:
    def candy(self, ratings) -> int:
        '''

        :param ratings: : List[int]
        :return:
        '''
        l = len(ratings)
        if l == 1:
            return 1
        resList = [0]*l
        rank = sorted(range(len(ratings)), key=lambda k: ratings[k])
        print(rank)
        for index in rank:
            if index >0 and index<l-1:

                if ratings[index-1]<ratings[index]:
                    if ratings[index+1]>=ratings[index]:
                        resList[index] = resList[index-1]+ 1

                    else:
                        resList[index] = max(resList[index-1],resList[index+1])+1



                elif ratings[index-1]==ratings[index]:

                    if ratings[index+1]<ratings[index]:
                        resList[index] = resList[index+1]+1
                    elif ratings[index+1]>=ratings[index]:
                        resList[index]=1

                else:
                    if ratings[index+1]>ratings[index]:
                        resList[index]=1
                    elif ratings[index+1]==ratings[index]:
                        resList[index]=max(1,resList[index+1])
                    else:
                        resList[index] = resList[index+1]+1



            elif index ==0:
                if ratings[index+1]<ratings[index]:
                    resList[index]=resList[index+1]+1

                else:
                    resList[index]=1
            else:
                if ratings[index-1]<ratings[index]:
                    resList[index]=resList[index-1]+1

                else:
                    resList[index]=1
        res = 0
        for i in range(l):
            res += resList[i]
        return res,resList



if __name__ == '__main__':
    ratings = [1,6,10,8,7,3,2]
    s = Solution()
    print(s.candy(ratings))
