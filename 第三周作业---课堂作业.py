#1.��ȡ�û���������֣�name�������䣨age��������һ�¸��û�����һ��Ϊ100��

def years():
    name=input("name:")
    year=int(input("age:"))
    years=2018-year+100
    print("%s��%d��100��!" %(name,years))


years()

#2.��ȡ�û��������������������������ӡ������������������������ż�����ӡ�����������ż����

def judge():
    number = int(input("����һ������:"))
    if number % 2 == 0:
        print("���������ż��")
    elif number % 2 == 1:
        print("�������������")
    else:
        print("���������0")

judge()

#3.���������һ�� list���жϸ� list ���Ƿ��пն������������ַ���ʵ�֣�
#һ��
def judgelist(list):
    print(all(list))

judgelist([0,''])
#����
def judgelist(list):
    if list:
        print('list is ture')
    else:
        print('list is false')

judgelist([])
#����
def judgelist(list):
    if 0 == len(list):
        print('list is false')
    else:
        print('list is ture')

judgelist([])

#4.���������һ�������б��Ѹ��б���ÿ��������ƽ���󷵻��µ��б����������ַ���ʵ�֣�

#һ��
lst = [1,2,3,4]
def judgeint(lst):
    lst2 = [x * 2 for x in lst]
    print(lst2)

judgeint(lst)
#����
lst = [1,2,3,4]
def judgeint(lst):
    lst2 = map(lambad x : �� * 2,lst)
    print(list(lst2))

judgeint(lst)


#5.���������һ�������б�ʹ�� reduce ����ʵ����ͺ󷵻ؽ��

lst = [1,2,3,4]
def list2(lst):
    print(reduce(lambda x,y : x + y,lst))

list2(lst)

#6.�����б��Ƶ�ʽʵ������
lst = [1,2,3,4]
def list3(lst):
    lst2 = [x * x * x for x in lst]
    print(lst2)

list3(lst)

#7.������������� list���뷵�����ǵĹ�ͬԪ������ɵ����б�
lst1 = [1,2,4]
lst2 = [3,6,8]
def list4(lst1 , lst2):
    print(list(zip(lst1,lst2)))

list4(lst1,lst2)

#8.�ҳ����������е�����������������ַ���ʵ�֣�

#һ��
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

#����
import math
def max3(x,y,z):
    return print(max(x,y,z))

max(1,9,2)