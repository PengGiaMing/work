#1.获取用户输入的名字（name）和年龄（age），计算一下该用户到哪一年为100岁

def years():
    name=input("name:")
    year=int(input("age:"))
    years=2018-year+100
    print("%s到%d年100岁!" %(name,years))


years()

#2.获取用户输入的整数，如果它是奇数则打印”您输入的是奇数”，如果是偶数则打印”您输入的是偶数”

def judge():
    number = int(input("输入一个数字:"))
    if number % 2 == 0:
        print("你输入的是偶数")
    elif number % 2 == 1:
        print("你输入的是奇数")
    else:
        print("你输入的是0")

judge()

#3.输入参数是一个 list，判断该 list 中是否有空对象（至少用三种方法实现）
#一：
def judgelist(list):
    print(all(list))

judgelist([0,''])
#二：
def judgelist(list):
    if list:
        print('list is ture')
    else:
        print('list is false')

judgelist([])
#三：
def judgelist(list):
    if 0 == len(list):
        print('list is false')
    else:
        print('list is ture')

judgelist([])

#4.输入参数是一个整数列表，把该列表中每个整数都平方后返回新的列表（至少用两种方法实现）

#一：
lst = [1,2,3,4]
def judgeint(lst):
    lst2 = [x * 2 for x in lst]
    print(lst2)

judgeint(lst)
#二：
lst = [1,2,3,4]
def judgeint(lst):
    lst2 = map(lambad x : ｘ * 2,lst)
    print(list(lst2))

judgeint(lst)


#5.输入参数是一个整数列表，使用 reduce 函数实现求和后返回结果

lst = [1,2,3,4]
def list2(lst):
    print(reduce(lambda x,y : x + y,lst))

list2(lst)

#6.请用列表推导式实现立方
lst = [1,2,3,4]
def list3(lst):
    lst2 = [x * x * x for x in lst]
    print(lst2)

list3(lst)

#7.输入参数是两个 list，请返回它们的共同元素所组成的新列表
lst1 = [1,2,4]
lst2 = [3,6,8]
def list4(lst1 , lst2):
    print(list(zip(lst1,lst2)))

list4(lst1,lst2)

#8.找出三个整数中的最大数（至少用两种方法实现）

#一：
def max2():
    num1 = int(input("num1:"))
    num2 = int(input("num2:"))
    num3 = int(input("num3:"))
    if num1 > num2:
        if num1 > num3:
            print("max:%d" %(num1))
        else:
            print("max:%d" %(num3))
    else:
        if num2 > num3:
            print("max:%d" %(num2))
        else:
            print("max:%d" %(num3))

max2()

#二：
import math
def max3(x,y,z):
    return print(max(x,y,z))

max(1,9,2)