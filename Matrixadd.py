R = int(input("Enter the number of rows of A: "))
P = int(input("Enter the number of columns of A: "))

Q = int(input("Enter the number of rows of B: "))
S = int(input("Enter the number of columns of B: "))

A = []
B = []

for i in range(R):
    Arow = []
    for j in range(P):
        a = int(input(f"Enter the {j + 1} element of row {i + 1} of A: "))
        Arow.append(a)
    A.append(Arow)

for k in range(Q):
    Brow = []
    for l in range(S):
        b = int(input(f"Enter the {l + 1} element of row {k + 1} of B: "))
        Brow.append(b)
    B.append(Brow)

C = []

for i in range(R):
    Crow = []
    for j in range(P):
        Crow.append(A[i][j] + B[i][j])
    C.append(Crow)

print("Resultant Matrix C:")
for row in C:
    print(row)
