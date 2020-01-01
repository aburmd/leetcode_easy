"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        pw={0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
        arr=[]
        while 1!=2:
            isHappy=0
            res=''
            pre=sorted(str(n),reverse=False)
            for j in pre:
                if j!='0':
                    res+=j
            if res not in arr:
                arr.append(res)
            else:
                arr.append(res)
                return False
            for i in res:
                isHappy+=int(pw[int(i)])
            if isHappy==1:
                return True
            n=isHappy


"""
FirstCommit: 
Runtime: 32 ms, faster than 81.46% of Python3 online submissions for Happy Number.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Happy Number.
"""