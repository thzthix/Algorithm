import sys
# 세개씩 끊어서 정해준다. 65~68: 3초, 69~71: 4초...
str = input()
sum = 0
for c  in str:
    a = ord(c)
    if (a<=67):
        sum +=3
    elif (a<=70):
        sum+=4
    elif (a<=73):
        sum+=5
    elif(a<=76):
        sum+=6
    elif(a<=79):
        sum+=7
    elif(a<=83):
        sum+=8
    elif(a<=86):
        sum+=9
    else:
        sum+=10
print(sum)
        