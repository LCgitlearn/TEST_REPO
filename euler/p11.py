nums = []
re = open("test/longNum2")
for i in xrange(20):
    nums.append(re.readline().replace("\n", "").split(" "))
re.close()
maxNum = 0
loopNum = 4
for i in xrange(20 - loopNum):
    for j in xrange(20 - loopNum):
        result = 1
        for n in xrange(loopNum):
            result *= int(nums[i][j + n])
            if(maxNum < result):
                maxNum = result
        #     print(nums[i][j + n]),
        # print result
print maxNum

# maxNum = 0
for i in xrange(20 - loopNum):
    for j in xrange(20 - loopNum):
        result = 1
        for n in xrange(loopNum):
            result *= int(nums[i + n][j])
            if(maxNum < result):
                maxNum = result
        #     print(nums[i + n][j]),
        # print result
print maxNum

# maxNum = 0
for i in xrange(20 - loopNum):
    for j in xrange(20 - loopNum):
        result = 1
        for n in xrange(loopNum):
            result *= int(nums[i + 3 - n][j + n])
            if(maxNum < result):
                maxNum = result
        #     print(nums[i + 3 - n][j + n]),
        # print result
print maxNum

# maxNum = 0
for i in xrange(20 - loopNum):
    for j in xrange(20 - loopNum):
        result = 1
        for n in xrange(loopNum):
            result *= int(nums[i + n][j + n])
            if(maxNum < result):
                maxNum = result
        #     print(nums[i + n][j + n]),
        # print result
print maxNum
