def min_cost_path(grid: list[list[int]]) -> int:
    dp = grid
    
    cols = len(grid[0])
    rows = len(grid)
    
    dp = []
    for i in range(rows):
        dp.append([0] * cols)
        
    dp[0][0] = grid[0][0]
     
    for j in range(1 , cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
            
    return dp[rows - 1][cols - 1]
            
grid = [ [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1] ]

print(min_cost_path(grid))