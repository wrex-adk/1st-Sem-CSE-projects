
R = int(input("Enter the number of rows of A: "))
P = int(input("Enter the number of columns of A: "))

A = []
    
for i in range(R):
        Arow=[]
        for j in range(P):
            a = int(input(f"Enter the {j + 1} element of row {i + 1} of A: "))
            Arow.append(a)
        A.append(Arow)  
if A[2][1]  0 :
    print("The given matrix is upper triangular")
else:
    print("The given matrix is not upper triangular")

          
    