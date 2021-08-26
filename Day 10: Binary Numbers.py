#!/bin/python3

import math
import os
import random
import re
import sys

    
if __name__ == '__main__':
    n = int(input().strip())
    
    num = []
    
    while n > 0:
        rm = n % 2
        n = n//2
        num.append(rm)
    
    count = 0
    result = 0
    
    for i in range(0,len(num)):
        if num[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)
    
    print(result)
    
