# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:31:37 2019

@author: terry
"""
import random
def simple_diff( x,y,z ):
    """
    x   题目数
    y   减法下限
    z   减数，被减数 上限
    """
    print("-----------Info---------------")
    print("题目数：\t%s" % x)
    print("题目类型：\t减法")
    print("题目难度：\t%s以内" % z)

    a = 0
    subtraction_list = []
    while a < x :  
        minuend = random.randint(0,z)
        subtrahend = random.randint(0,z)
        num_list = []
        num_list.append(minuend)
        num_list.append(subtrahend)
        DIFF = minuend - subtrahend
        question_dic = {}
        if DIFF >= y :
            question_dic['question'] = num_list
            question_dic['answer'] = DIFF
            subtraction_list.append(question_dic)
            a += 1
 
    print("-----------Question---------------")
    
    for i in subtraction_list:
        print(i['question'][0] ,"\t-  ",i['question'][1] ,"\t=\t" )
    
    print("\n-----------Ansewer---------------")  
    
    for i in subtraction_list:
        print(i['question'][0] ,"\t-  ",i['question'][1] ,"\t=\t" ,i['answer']) 
        
if __name__ == '__main__':
    simple_diff( 10,0,10 )
