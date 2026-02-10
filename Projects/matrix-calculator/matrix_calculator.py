def matrix_input():
    print("For matrix :")
    rows = int(input("rows: "))
    col = int(input("columns: "))
    mat=[]
    print("Entries Row-wise: ")
    for i in range(rows):
        row=[]
        for j in range(col):
            row.append(int(input("Enter the Element: ")))
        mat.append(row)
    return mat
def matrix_multiplication(mat1, mat2):
    if len(mat2)== len(mat1[0]):
        p=[[0]*len(mat2[0]) for _ in range(len(mat1))]
        for z in range(len(mat2)):
            for i in range(len(p)):
                for j in range(len(p[0])):
                    p[i][j] +=mat1[i][z]*mat2[z][j]
        return p
    else :
        return "Matrix multiplication not possible for the given matrices"
def matrix_add(mat1,mat2):
    if len(mat2)==len(mat1) and len(mat1[0])==len(mat2[0]):
        p=[[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))]for i in range(len(mat1))]
        return p
    else:
        return "Matrix addition not possible as the order of matrices is not same"
def matrix_subtract(mat1,mat2):
    if len(mat2)==len(mat1) and len(mat1[0])==len(mat2[0]):
        p=[[mat1[i][j]-mat2[i][j] for j in range(len(mat1[0]))]for i in range(len(mat1))]
        return p
    else:
        return "Matrix subtraction not possible as the order of matrices is not same"
def matrix_transpose(mat):
    p = [[0]*len(mat) for _ in range(len(mat[0]))]
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            p[i][j] = mat[j][i]
    return p
def scalar_mult(k,mat):
    p=[[k*mat[i][j] for j in range(len(mat[0]))]for i in range(len(mat))]
    return p
def matrix_trace(mat):
    p=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j :
                p = p + mat[i][j]
    return p
def get_minor(mat,i,j):
    return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]
def get_determinant(mat):
    if len(mat)!= len(mat[0]):
        return "Determinant not possible (non-square matrix)"
    else:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for c in range(n):
            minor = get_minor(mat, 0, c)
            det += ((-1)**c) * mat[0][c] * get_determinant(minor)
        return det
def print_matrix(mat):
    for r in mat:
        print(*r)

print("Please select operation -\n"
      "1. Add -\n"
      "2. Subtract\n"
      "3. Scalar Multiply\n"
      "4. Trace\n"
      "5. Transpose\n"
      "6. Matrix Multiply\n"
      "7. Determinent\n")

sel = int(input("Select operation (1-7): "))

if sel == 1:
    print("For matrix 1: ")
    mat1=matrix_input()
    print("For matrix 2: ")
    mat2=matrix_input()
    res=matrix_add(mat1,mat2)
    print_matrix(res)
    
elif sel == 2:
    print("For matrix 1: ")
    mat1=matrix_input()
    print("For matrix 2: ")
    mat2=matrix_input()
    res=matrix_subtract(mat1,mat2)
    print_matrix(res)
elif sel == 3:
    print("For matrix 1: ")
    mat1=matrix_input()
    k = int(input("Scalar for the multiplication: "))
    res = scalar_mult(k,mat1)
    print_matrix(res)
elif sel == 4:
    print("For matrix 1: ")
    mat1=matrix_input()
    res = matrix_trace(mat1)
    print(res)
elif sel == 5:
    print("For matrix 1: ")
    mat1=matrix_input()
    res = matrix_transpose(mat1)
    print_matrix(res)
elif sel == 6:
    print("For matrix 1: ")
    mat1=matrix_input()
    print("For matrix 2: ")
    mat2=matrix_input()
    res=matrix_multiplication(mat1,mat2)
    print_matrix(res)
elif sel == 7:
    print("For matrix 1: ")
    mat1=matrix_input()
    res =get_determinant(mat1)
    print(res)
else:
    print("Please select a number from the range")
