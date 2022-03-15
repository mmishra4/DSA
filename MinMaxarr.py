# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:57:57 2022

@author: MMEENAK4
"""

def MinMaxArr(A):
        N = len(A)
        Amin = min(A)
        Amax = max(A)
        print(Amax, Amin)
        mini = None
        maxi = None
        ans = N
        if(Amin == Amax): return 1
        for i in range(N-1, -1, -1):
            if A[i] == Amax:
                maxi = i
                print(maxi)
                if mini != None:
                    ans = min(ans, mini-maxi+1)
                    print(ans)
            elif A[i] == Amin:
                mini = i
                print(mini)
                if maxi != None:
                    ans = min(ans, maxi-mini+1)
                    print(ans)
        return ans


def MakeEleMax(A,B):
    N = len(A)
    cnt = 0
    if B in A:
        for i in range(N-1, -1, -1):
            if A[i] > B:
                cnt+=1
        return cnt
    else:
        return -1
    
            
            
    
# =============================================================================
# # Driver code
# A = [ 814, 761, 697, 483, 981 ]
# #A = [ 343, 291, 963, 165, 152 ]
# print ('MaxMin index is ', MinMaxArr(A))
# =============================================================================
A = [2, 4, 3, 1, 5]
B = 3
A = [1, 4, 2]
B = 3 
print(MakeEleMax(A,B)) 