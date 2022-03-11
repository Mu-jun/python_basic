#!/usr/bin/env python
# coding: utf-8

# In[ ]:


PI = 3.14

def number_input():
    output = input('숫자 입력 : ')
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius **2

print('test_module의 __name__ :',__name__)
if __name__ == '__main__':
    print('test_module :',get_circumference(10))
    print('test_module :',get_circle_area(10))

