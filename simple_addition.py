# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:30:29 2019

@author: terry
"""

import random

def simple_add( x,y,z ):
    """
    x   题目数
    y   加法上限
    z   加数，被加数
    """
    print("-----------Info---------------")
    print("题目数：\t%s" % x)
    print("题目类型：\t加法")
    print("题目难度：\t%s以内" % y)
    
    a = 0
    addition_list = []
    while a < x :  
        augend = random.randint(0,z)
        addend = random.randint(0,z)
        sum_list = []
        sum_list.append(augend)
        sum_list.append(addend)
        SUMM = sum(sum_list)
        question_dic = {}
        if SUMM <= y :
            question_dic['question'] = sum_list
            question_dic['answer'] = SUMM
            addition_list.append(question_dic)
            a += 1
    
    print("-----------Question---------------")
    
    for i in addition_list:
        print(i['question'][0] ,"\t+  ",i['question'][1] ,"\t=\t" )
    
    print("\n-----------Ansewer---------------")  
    
    for i in addition_list:
        print(i['question'][0] ,"\t+  ",i['question'][1] ,"\t=\t" ,i['answer'])
    

if __name__ == '__main__':
    simple_add( 10,20,99 )
    
