def tscheby (n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 
    return matrix
    # x = 2
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 2*x - 1
    # else:
    #     result = 2*tscheby(n-1)-tscheby(n-2)
    #     return result
n = 3
print tscheby(n)
