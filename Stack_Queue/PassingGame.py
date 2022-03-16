#There is a football event going on in your city. In this event, you are given A passes and players having ids between 1 and 106.
#Initially some player with a given id had the ball in his possession. You have to make a program to display the id of the player who possessed the ball after exactly A passes.
#There are two kinds of passes:
#1) ID
#2) 0
#For the first kind of pass, the player in possession of the ball passes the ball "forward" to player with id = ID.
#For the second kind of a pass, the player in possession of the ball passes the ball back to the player who had forwarded the ball to him.
#In the second kind of pass "0" just means Back Pass.
#Return the ID of the player who currently posseses the ball.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        stack = [B]
        for i in C:
            if i == 0:
                stack.pop()
            else:
                stack.append(i)
        return stack[-1]

