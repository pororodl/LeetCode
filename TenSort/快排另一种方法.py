# 设置两个指针i,j，i初始指向数组的第一个元素，j初始化为i+1,然后我们设定i指向的元素为基准数字
# 我们要做的是，在一趟快速排序中，把那些比基准数字小的数，移动到前面
# 具体的算法：
# 如果j指向的值大于等于基准数字（直接跳过） j+=1
# 如果j指向的值小于基准数字  先i+=1   再交换L[i]和L[j] 最后j+=1
# 一趟结束，这时候交换L[left],L[i],此时，基准数字就换到了i的位置，
# 递归[left,i-1] 和[i+1,right]  要注意递归的出口，就是当left<right，才能进行上面的步骤
# 参考 https://blog.csdn.net/u010429424/article/details/77776731

class Solution:
    def quick(self,L,left,right):

        if left < right:
            i = left
            j =i+1
            pivot = L[i]
            while j<len(L):
                if L[j]>=pivot:
                    j+=1
                else:
                    i+=1
                    L[i],L[j] = L[j],L[i]
                    j+=1
            L[left],L[i]=L[i],L[left]
            self.quick(L,left,i-1)
            self.quick(L,i+1,right)


if __name__ == '__main__':
    s = Solution()
    L = [4,2,5,3,7,9,0,1]
    s.quick(L,0,len(L))
    print(L)

