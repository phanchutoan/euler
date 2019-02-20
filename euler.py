import math


# Problem 4

def checkPalindromic( num ):
    numString = str(num)
    if len(numString)%2 != 0:
        return False
    else:
        firstHalf = numString[:len(numString)/2]
        laterHalf = numString[len(numString)/2:][::-1]
        return firstHalf == laterHalf

def problem_4():
    num = 1001

    breakCheck = False
    max = -1
    max_x = -1
    max_y = -1

    for i in range(999,0,-1):
        if breakCheck == True:
            break
        for x in range(999,0,-1):
            if (checkPalindromic(i*x)):
                if (i*x > max):
                    max = i*x
                    max_x = x
                    max_y = i
                # print(x*i)
                # print(x)
                # print(i)
                # breakCheck = True
                break

    print(max)
    print(max_x)
    print(max_y)





# total = 0

# for x in range(0, 1000):
#     if x%3==0 or x%5==0:
#         total = total + x 
#         print(x)


# print (total)


# a = 1
# b = 2
# total = 2
# c = 0
# while c < 4000000:
#     c = a + b
#     a = b
#     b = c
#     if (c%2 == 0):
#         total = total + c
#         print (c)

# print(total)


# What is the largest prime factor of the number 600851475143 ?


# num = int(25698751364526)
         
# breakCheck = False

# for x in range(2, int(math.sqrt(num)) + 1):
#     if(breakCheck == False):
#         xIsPrime = True
#         for y in range(2,int(math.sqrt(x)) + 1):
#             if x%y == 0:
#                 xIsPrime = False
#                 continue
#         if(xIsPrime):
#             while (num%x==0):
#                 print ("deviding: " + str(x))
#                 num = num/x
#                 print ("num now: "+ str(num))
#                 print (str(x) + " is prime")
#                 if num == 1:
#                     breakCheck = True

def getPrimeNumbersSmallerThan(num):
    breakCheck = False
    list = []
    for x in range(2, num):
        if(breakCheck == False):
            xIsPrime = True
            for y in range(2,x):
                if x%y == 0:
                    xIsPrime = False
                    continue
            if(xIsPrime):
                list.append(x)
    return list
                

def problem_5():
    # 1. Phan tich cac so tu 1-20 thanh so nguyen to
    # tim bac cao nhat cua cac so nguyen to < 20
    # nhan cac ket qua voi nhau
    print(getPrimeNumbersSmallerThan(20))

if __name__ == '__main__':
    problem_5()