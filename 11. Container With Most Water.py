def maxArea(height):
    l = len(height)
    prior = 0
    post = l - 1
    maxWater = 0
    while prior != post:
        curMIN= min(height[prior],height[post])
        maxWater = max(curMIN*(post-prior),maxWater)
        if curMIN==height[prior]:
            prior+=1
        else:
            post-=1
    return maxWater



if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))
