#time: O(n)
#space: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        d=0 #ptr for dirs array
        x=0
        y=0
        #iterating the instructions
        for c in instructions:
            if c=='R':
                d=(d+1)%4
            elif c=='L':
                d=(d+3)%4
            else:
                x+=dirs[d][0]
                y+=dirs[d][1]
        #checking if it's at origin or direction is not North
        if d!=0 or (x==0 and y==0):
            return True
        return False
       
