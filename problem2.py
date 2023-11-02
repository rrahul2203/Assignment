class Solution:
    # @param grid: array of string
    # @return an integer
    def minSideLengthSquareFrame(self, grid):
        n, m = len(grid), len(grid[0])
        x_min, y_min = n, m

        x_max, y_max = -1, -1
        marked_cells = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':
                    x_min = min(i, x_min)
                    y_min = min(j, y_min)
                    x_max = max(i, x_max)
                    y_max = max(j, y_max)
                    marked_cells.append((i, j))
        
        ## If there is no marked cell, return 1 "Impossible"
        if len(marked_cells)==0:
            return 1

        ## If there is only one marked cell present 
        if x_max == x_min and y_max == y_min:
            i_min = max(x_min-2, 0)
            j_min = max(y_min-2, 0)
            for i in range(i_min, x_max+1):
                for j in range(j_min, y_max+1):
                    xcorner_point = i + 2
                    ycorner_point = j + 2
                    if xcorner_point >= n or ycorner_point >= m:
                        continue

                    if (x_min == i or x_min == xcorner_point) and (y_min >= j and y_min <= ycorner_point):
                        return 3
                    if (y_min == j or y_min == ycorner_point) and (x_min >= i and x_min <= xcorner_point):
                        return 3
            return 1
        
        
        # For all the marked cells are present in either veritical or horizontal straight line
        if x_max == x_min or y_max == y_min:
            const = max(2, y_max - y_min, x_max - x_min)
            if x_min == x_max:
                if  (x_min + const) < n:
                    return const + 1
                elif (x_min - const) >= 0:
                    return const + 1  
            else:
                if (y_min + const) < m:
                    return const + 1
                elif (y_min - const) >= 0:
                    return const + 1
            return 1
        
        possible_sidelength = max(x_max-x_min, y_max-y_min, 2) + 1
        
        ## Assuming the cells are marked as 'X' on the edges of square frame
        ## There cannot be more than 4*(length of square frame - 1) for a valid
        ## square frame
        if len(marked_cells) > 4*(possible_sidelength-1):
            return 1
        
        ## For other cases - where points are present on two or more edges of the square frame
        if x_max - x_min > y_max - y_min:
            i_min, i_max = x_min, x_max
            j_min = max(y_max - possible_sidelength + 1 , 0)
            j_max = min(y_min + possible_sidelength - 1, m-1)
        elif x_max - x_min < y_max - y_min:
            j_min, j_max = y_min, y_max
            i_min = max(x_max - possible_sidelength + 1, 0)
            i_max = min(x_min + possible_sidelength - 1, n-1)
        else:
            i_min, i_max, j_min, j_max = x_min, x_max, y_min, y_max

        
        ## Sliding window to check the valid window for the possible length
        ## Although there are 3 loops here, but the loop for i or j remains only one time
        ## depending on which dimension is fixed (either length or width)
        ## So, TC - O(m*n)
        ## SC - O(m+n)
        for i in range(i_min, i_max - possible_sidelength + 2):
            for j in range(j_min, j_max - possible_sidelength + 2):
                xcorner_point = i + possible_sidelength - 1
                ycorner_point = j + possible_sidelength - 1
                if xcorner_point >= n or ycorner_point >= m:
                    continue

                flag = True
                for cell in marked_cells:
                    row, col = cell
                    if (row >= i_min and row<= xcorner_point) and (col==j or col==ycorner_point):
                        flag = True
                    elif (col >= j_min and col<= ycorner_point) and (row==i or row==xcorner_point):
                        flag = True
                    else:
                        flag = False
                    
                    ## if a point is on the assumed square frame
                    if not flag:
                        break

                if flag:
                    return possible_sidelength
        
        return 1
    

if __name__ == "__main__": 
    obj = Solution()
    with open('input2.txt', 'r') as file:
        # Read the first line to get the number of test cases
        num_test_cases = int(file.readline().strip())

        # Read the test cases one by one
        for n in range(num_test_cases):
            line = file.readline().strip()
            n, m = list(map(int, line.split()))
            grid = []
            while n>0:
                line = file.readline().strip()
                grid.append(line)
                n -= 1

            ans = obj.minSideLengthSquareFrame(grid)
            print(grid)
            print(ans)
    