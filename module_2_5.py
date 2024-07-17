def get_matrix(n, m, value):
    matrix = []
    if value > 0 and n > 0 and m > 0:
        for i in range(n):
            x = []
            for j in range(m):
                x.append(value)
            matrix.append(x)
    print(matrix)
get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
