num = 0
nextNum = 1
result = 0
while True:
    num += nextNum
    nextNum += num
    if(num%2 == 0):
        result += num
    if(num > 4000000): break
    if(nextNum%2 == 0):
        result += nextNum
    if(nextNum > 4000000): break
print result
