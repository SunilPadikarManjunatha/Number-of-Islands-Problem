class Solution:
    def numIslands(self, grid) -> int:
        
        row = len(grid)
        col = len(grid[0]) if row else 0
        islands = 0
        cons = []
        for i in range(row):
            for j in range(col):
                
                if grid[i][j] == "1":
                    self.check(grid,i,j, row,col)
                    islands +=1
        print(islands)
        return islands

    def check(self, grid, i,j, row,col):
        if i >=0 and i < row and j >=0 and j < col and grid[i][j] == "1":
            grid[i][j] = "V"
            print(grid)
            self.check(grid,i-1,j,row,col)
            self.check(grid,i+1,j,row,col)
            self.check(grid,i,j-1,row,col)
            self.check(grid,i,j+1,row,col)

# grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# grid = [["1","1"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
sol = Solution()

print(sol.numIslands(grid))