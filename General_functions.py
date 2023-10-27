import math

def crossvector(c, d, b):
    c[0] = d[1] * b[2] - d[2] * b[1]
    c[1] = d[2] * b[0] - d[0] * b[2]
    c[2] = d[0] * b[1] - d[1] * b[0]

def innerproduct(n1, n2):
    return n1[0] * n2[0] + n1[1] * n2[1] + n1[2] * n2[2]

def vectorlength(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

def vectorlength_squared(v):
    return v[0] * v[0] + v[1] * v[1] + v[2] * v[2]

def sign_function(x):
    if x < 0:
        return -1.0
    return 1.0

def periodiccondition(dx):
    if dx > Lbox / 2.0:
        return dx - (Lbox + 1.0)
    elif dx < -Lbox / 2.0:
        return (Lbox + 1.0) + dx
    else:
        return dx

def vector_transformation(MV, M, V):
    MV[0] = M[0][0] * V[0] + M[0][1] * V[1] + M[0][2] * V[2]
    MV[1] = M[1][0] * V[0] + M[1][1] * V[1] + M[1][2] * V[2]
    MV[2] = M[2][0] * V[0] + M[2][1] * V[1] + M[2][2] * V[2]
