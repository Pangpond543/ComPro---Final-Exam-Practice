def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                S = [i, j]
            if maze[i][j] == "E":
                E = [i, j]
    # print(E)     
        
    walk = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    
    con = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
    
    p = S.copy()
    path_ = [p]
    dis_t = 0
    
    
    # print(p)
    while path_[-1] != E:
        for w in walk:
            n_walk = [p[0] + w[0], p[1] + w[1]]
            
            if n_walk[0] < 0 or n_walk[1] < 0 or n_walk[0] > len(maze)-1 or n_walk[1] > len(maze[0])-1 or maze[n_walk[0]][n_walk[1]] == "#" or n_walk in path_:
                continue
            
            # print(p)
            dis_t += 1
            p = [n_walk[0], n_walk[1]]
            path_.append([p[0], p[1]])
            
            # print(dis_t, "dis")
            
            if maze[p[0]][p[1]] in con:
                con_w = con[maze[p[0]][p[1]]]
                while maze[p[0]][p[1]] in con and maze[p[0] + con_w[0]][p[1] + con_w[1]] != "#":
                    p = [p[0] + con_w[0], p[1] + con_w[1]]
                    if 0 <= p[0] < len(maze) and 0 <= p[1] < len(maze[1]):
                        path_.append([p[0], p[1]])
                    
            break
        else : 
            return {'distance': -1, 'path': []}
        
    # print(path_)
    # print(dis_t)
    
    return {'distance': dis_t, 'path': path_}


if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}


    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}
