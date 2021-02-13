#########################################################
#                -==John Folsonner==-                   #
#             -==14 task of the exam==-                 #
#########################################################

# /IMPORT BLOCK/
import math
# /IMPORT BLOCK/

# /DEF BLOCK/
def convert(num, to_base=2):
    conv_num = 0
    X = 1
    while num:
        conv_num += (num % to_base) * X
        X *= 10
        num //= to_base
    return conv_num

def sum(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s

def IsPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
# /DEF BLOCK/

# /Variable block/
SUMM = 0
n = int(input())
# /Variable block/

for i in range(2, 11):
    num = convert(n, to_base=i)
    if IsPrime(sum(num)) == True:
        SUMM += i

print(SUMM)
