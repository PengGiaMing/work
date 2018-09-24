1.

import random
import string

user_list = []

def judge1():
    user_txt = input("请输入你的密码内容:")
    user_length = int(input("请输入你的密码长度:"))
    for i in range(user_length):
        password = random.choice(user_txt)
        user_list.append(password)
        result = "".join(user_list)
    print(f"系统为你生成的随机密码为:{result}")
    del result
    gc.collect()

judge1()

2.

def judge2(number,lst):
	b=-1
	c=0
	d=[]
	for a in lst:
		if a==number:
			print("列表里有元素%d" %(number))
			c=1
			break
	if c==0:
		print("列表里不存在元素%d" %(number))
	else:
            b = lst.index(number,b+1)
            d.append(b)
            for a in d:
	        if (len(lst) - 1) / 2 > a:
		    print("左边有一个")
		elif (len(lst)-1) / 2 < a:
	            print("右边有一个")
		else:
		    print("正好在中间有一个")

3.


import math
def fil(n):
    flag = 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            flag = 1
            break
    if flag == 1:
        return n

print(list(filter(fil,range(1,101))))

4.

import demo
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)

5.

def min5(lst):
    n = sorted(set(lst))
    print(n[0])

min5([9,3,8,1,0,3,5])
          
