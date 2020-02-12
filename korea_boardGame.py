import sys

try:
    inVar = sys.stdin.readline().rstrip()
    cnt = 0
    orgNum = inVar
    num = inVar

    if(int(num) >= 0 and int(num)<=99):
        if(int(num) < 10):
            num = '0'+num

        while True:
            tmp = num
            num = int(num[0]) + int(num[1])
            num = tmp[1]+str(num)
            cnt = cnt+1

            if(int(num) == int(orgNum)):
                break
    print(cnt)
except: exit()
