R = int(input("Enter the number of rows of A: "))
P = int(input("Enter the number of columns of A: "))

Q = int(input("Enter the number of rows of B: "))
S = int(input("Enter the number of columns of B: "))

# Check if multiplication is possible
if P != Q:
    print("Matrix multiplication is not possible")
else:
    A = []
    B = []

    # Input matrix A
    for i in range(R):
        Arow = []
        for j in range(P):
            a = int(input(f"Enter the {j + 1} element of row {i + 1} of A: "))
            Arow.append(a)
        A.append(Arow)

    # Input matrix B
    for k in range(Q):
        Brow = []
        for l in range(S):
            b = int(input(f"Enter the {l + 1} element of row {k + 1} of B: "))
            Brow.append(b)
        B.append(Brow)

    # Initialize resultant matrix C with zeros
    C = [[0] * S for _ in range(R)]

    # Perform matrix multiplication
    for i in range(R):
        for j in range(S):
            for k in range(P):  # or range(Q), since P == Q
                C[i][j] += A[i][k] * B[k][j]  # Correct dot product calculation

    # Print the resultant matrix C
    print("Resultant Matrix C:")
    for row in C:
        print(row)

