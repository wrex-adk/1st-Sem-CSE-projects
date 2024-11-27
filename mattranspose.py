
R = int(input("Enter the number of rows: "))
P = int(input("Enter the number of columns: "))
    
A = []
    

for i in range(R):
        Arow = []
        for j in range(P):
            a = int(input(f"Enter the {j + 1} element of row {i + 1} of A: "))
            Arow.append(a)
        A.append(Arow)

C = []

for i in range(R):
    Crow = []
    for j in range(P):
        Crow.append(A[j][i])
    C.append(Crow)

print("The resultant matrix is: ")
for row in C:
     print (row)
