#1.��дһ��������������������Ĺ��ܣ�������������볤�Ⱥ�������ɵ����ݣ�
#  ������ɵ����ݿ����д�д��ĸ��A-Z����Сд��ĸ��a-z�������֣�0-9����������ţ�~!@#$%^&*()����
#  ����ֵΪ�����û�Ҫ�����ɵ��������

import random
import string

user_list = []

def judge1():
    user_txt = input("�����������������:")
    user_length = int(input("������������볤��:"))
    for i in range(user_length):
        password = random.choice(user_txt)
        user_list.append(password)
        result = "".join(user_list)
    print(f"ϵͳΪ�����ɵ��������Ϊ:{result}")
    del result
    gc.collect()

judge1()

#2.�������Ϊһ�������б��һ���������жϸ������Ƿ�����ڸ��б��С�������ڣ������б�����߻����Ұ��

def judge2(number,lst):
	b=-1
	c=0
	d=[]
	for a in lst:
		if a==number:
			print("�б�����Ԫ��%d" %(number))
			c=1
			break
	if c==0:
		print("�б��ﲻ����Ԫ��%d" %(number))
	else:
            b = lst.index(number,b+1)
            d.append(b)
            for a in d:
	        if (len(lst) - 1) / 2 > a:
		    print("�����һ��")
		elif (len(lst)-1) / 2 < a:
	            print("�ұ���һ��")
		else:
		    print("�������м���һ��")

#3.����1-100�е�����

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

#4.��дһ��ģ�飬
#  Ҫ�������б���x��y���������add(x, y)���������sub(x, y)���������mul(x, y)���������div(x, y)���ĸ�������ʵ��

import demo
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)

#5.���������һ�������б����ҳ����б�����С������������

def min5(lst):
    n = sorted(set(lst))
    print(n[0])

min5([9,3,8,1,0,3,5])
          