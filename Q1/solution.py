## Add code below with answer clearly stated

from math import factorial


class Solution:
    def factorial_sum(num):
        sum=1
        output=0

        for i in reversed(range(1,int(num))):
            sum*=i


        for ch in str(sum):
            output+=int(ch)
        return output

    print(factorial_sum(100))