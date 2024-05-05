
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m_index = []

    for index, i in enumerate(matrix):
        for index_j,j in enumerate(i):
            if j==0:
                m_index.append([index, index_j])
    ro, col = zip(*m_index)
    print(ro,col)
    ro,col = set(ro), set(col)
    for i in ro:
        matrix[i] = [0] * len(matrix[0])
    for i in matrix:
        for j in col:
            i[j] = 0
    return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = setZeroes(matrix)
print(matrix)