import sys

class Solution:
    # @param grid: array of string
    # @return an integer
    def minChanges(self, line: str) -> int:
        # # Method 1 - TC- O(N), SC-O(N)
        # N = len(line)
        # white = [0]*(N+1)
        # black = [0]*(N+1)
        # for index in range(N):
        #     if line[index]=='0':
        #         white[index+1] = white[index] + 1
        #         black[index+1] = black[index]
        #     elif line[index]=='1':
        #         black[index+1] = black[index] + 1
        #         white[index+1] = white[index]
        

        # res = sys.maxsize
        # for partition in range(N):
        #     res = min(res, white[partition] +  black[N]-black[partition], black[partition] + white[N]-white[partition])
        
        # Method 2 - TC-O(N), SC-0(1)
        N = len(line)
        total_white = 0
        total_black = 0
        for index in range(N):
            if line[index]=='W':
                total_white += 1
            elif line[index]=='B':
                total_black += 1

        res = sys.maxsize
        white_count, black_count = 0, 0
        for index in range(N):
            res = min(res, white_count + total_black - black_count, black_count + total_white - white_count)
            if line[index]=='W':
                white_count += 1
            else:
                black_count += 1
        
        res = min(res, white_count + total_black - black_count, black_count + total_white - white_count)

        return res


if __name__ == "__main__": 
    # Driver code
    obj = Solution()

    # Open the input file
    with open('input1.txt', 'r') as file:
        # Read the first line to get the number of test cases
        num_test_cases = int(file.readline().strip())

        # Read the test cases one by one
        for _ in range(num_test_cases):
            test_case = file.readline().strip()
            output = obj.minChanges(test_case)
            print(test_case, "-------->", output)