import math

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    #create temp arr
    L = [0]*(n1 + 1 )
    R = [0]*(n2 + 1 )

    #copy data to L and R
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+1+j]

    
    #set sentinel value
    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0

    #merge back to A

    for k in range(p,r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def merge_sort(A,p,r):
    if p < r:
        q = (p + r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

            

# Example usage
A = [8, 4, 5, 2, 9, 1]
print("unsorted array : ",A)
merge_sort(A, 0, len(A) - 1)
print("Sorted array : ",A)
