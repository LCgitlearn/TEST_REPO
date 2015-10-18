import p5
num = open("test/longNum").read()
maxNum = 0
for i in xrange(1000 - 13):
    if("0" in num[i : i + 13]):
        continue
    mulResult = p5.mul([int(x) for x in num[i : i + 13]])
    if(maxNum < mulResult):
        maxNum = mulResult
print maxNum
