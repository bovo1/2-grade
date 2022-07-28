def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])

def total(A):
    T = 0
    for x in A:
        T += x
    return T

def cs():
    c_sum = 0
    for i in range(len(x)):
        if x[i] == 1:
            c_sum += A[i]
    return c_sum

def subset_sum(k):
    global i
    a_total = total(A)
    v_sum = cs()

    if k == len(A):
        if v_sum == S:
            print_subset(x)
            i = 0
    else:
        if v_sum + A[k] <= S:
            x[k] = 1
            subset_sum(k+1)
        x[k] = 0
        subset_sum(k+1)
    #print(i)

i = 1
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input())
x = [0] * len(A)
subset_sum(0)
if(i == 1): print([])
