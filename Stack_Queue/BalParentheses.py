#Given a string A consisting only of '(' and ')'.
#You need to find whether parentheses in A are balanced or not, if it is balanced then return 1 else return 0.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Initialising Variables
        flag = 1
        count = 0
    
        # Traversing the Expression
        for i in range(len(A)):
            if (A[i] == '('):
                count += 1
            else:
                
                # It is a closing parenthesis
                count -= 1
    
            if (count < 0):
    
                # This means there are 
                # more closing parenthesis 
                # than opening
                flag = 0
                break
    
        # If count is not zero , 
        # it means there are more 
        # opening parenthesis
        if (count != 0):
            flag = 0
    
        return flag
