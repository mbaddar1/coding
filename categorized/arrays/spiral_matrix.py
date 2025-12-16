
from typing import List
# status - ok but still some cases that fails
# https://leetcode.com/problems/spiral-matrix/submissions/1857256349

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        N = n*m
        i = 0
        j = 0
        count = 0
        spiral_order = []
        left_wall = 0
        right_wall = m-1
        bottom_wall = n-1
        upper_wall = 0
        direction = "right"
        # print(f"N={N}")
        while count <N:
            # print(i,j)
            c = matrix[i][j]
            spiral_order.append(c)
            # print(spiral_order)
            count += 1
            # print(f"count = {count}")
            # if count ==N:
            #     break
            i,j,left_wall,right_wall,upper_wall,bottom_wall,direction = Solution.update(i, j,left_wall,right_wall,upper_wall,bottom_wall,direction)
        # print(len(spiral_order))
        return spiral_order
    @staticmethod
    def update(i:int,j:int,left_wall:int,right_wall:int,upper_wall:int,bottom_wall:int,direction:str):
        if i == upper_wall and j==right_wall and direction == "right":
            upper_wall=+1
            direction="down"
        elif i==bottom_wall and j==right_wall and direction == "down":
            right_wall= right_wall-1
            direction="left"
        elif j==left_wall and i==bottom_wall and direction == "left":
            bottom_wall=bottom_wall-1
            direction="up"
        elif i==upper_wall and j==left_wall and direction == "up":
            left_wall=+1
            direction="right"

        if direction == "right":
            j = j+1
        elif direction == "left":
            j = j-1
        elif direction== "down":
            i = i+1
        elif direction== "up":
            i = i-1
        else:
            raise ValueError
        return i,j,left_wall,right_wall,upper_wall,bottom_wall,direction




if __name__=="__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
    sol = Solution()
    r = sol.spiralOrder(matrix)
    print(r)
    #  [1,2,3,4,8,12,11,10,9,5,6,7]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # sol = Solution()
    # r = sol.spiralOrder(matrix)
    # print(r)


