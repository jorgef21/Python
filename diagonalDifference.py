def diagonalDifference(n,arr):
    left = 0
    right = 0
    i=0
    while i != n:
        left+=arr[i][i]
        right+=arr[i][n-1-i]
        i+=1
   
    return abs(left-right)

if  __name__=='__main__':
    n = 3
    arr = [[11,2,4],[4,5,6],[10,8,-12]]
    print(diagonalDifference(n,arr))
