first = 999
second = 999
firstMinLine = 100
secondMinLine = 100
maxPalindrome = 0
memoFirst = 0
memoSecont = 0
while True:
    num = first * second
    if(str(num) == str(num)[::-1]):
        if maxPalindrome < num:
            maxPalindrome = num
            memoFirst = first
            memoSecond = second
        secondMinLine = second
        second -= 1
        secondMinLine = second
    elif(second > secondMinLine):
        second -= 1
    elif(first > firstMinLine):
        second = 999
        first -= 1
    else:
        break
print maxPalindrome
print str(memoFirst) +" : "+ str(memoSecond)
