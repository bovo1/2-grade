import random, timeit, time

def quickSort(A, first, last):
    global Qc, Qs
    if first >= last:
        Qc += 1
        return
    left, right = first + 1, last
    pivot = A[first]

    while left <= right:
        Qc += 1
        while left <= last and A[left] < pivot:
            Qc += 1
            left += 1
        Qc += 1
        while right > first and A[right] >= pivot:
            Qc += 1
            right -= 1
        Qc += 1
        Qc += 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
    Qc += 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quickSort(A, first, right-1)
    quickSort(A, right +1, last)

def mergeSort(A, first, last):
    global Mc, Ms
    Mc += 1
    if first >= last: return
    m = (first+last)//2
    mergeSort(A, first, m)
    mergeSort(A, m+1, last)
    B = []
    i = first
    j = m+1

    while i <= m and j <= last:
        Mc += 1
        Mc += 1
        if A[i] <= A[j]:
            B.append(A[i])
            Ms += 1
            i += 1
        else:
            B.append(A[j])
            Ms += 1
            j += 1
    Mc += 1
    for i in range(i, m+1):
        B.append(A[i])
        Ms += 1
    for j in range(j, last+1):
        B.append(A[j])
        Ms += 1
    for k in range(first, last+1):
        A[k] = B[k-first]
        Ms += 1

def make_heap(A, n):
    for k in range(n-1, -1, -1):
        heapify(A, n, k)

def heapify(A, n, k):
    global Hc, Hs
    l = 2*k + 1

    while l<n:
        Hc += 1
        l = 2*k + 1
        r = 2*k + 2
        Hc += 1
        if l<n and A[l] > A[k]:
            m = l
        else:
            m = k
        Hc += 1
        if r < n and A[r] > A[m]:
            m = r
        Hc += 1
        if m != k:
            A[k], A[m] = A[m], A[k]
            Hs += 1
            k = m
        else: break
    Hc += 1

def heapSort(A, n):
    global Hc, Hs
    make_heap(A, n)
    for k in range(n-1, 0, -1):
        A[0], A[k] = A[k], A[0]
        Hs += 1
        n -= 1
        heapify(A, n, 0)

def check_sorted(A):
    n = len(A)
    for i in range(n-1):
        if A[i] > A[i+1]: return False
    return True

Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
n = int(input())
random.seed()
q = []
for i in range(n):
    q.append(random.randint(-1000, 1000))
m = q[:]
h = q[:]

quickSort(q, 0, n-1)
mergeSort(m, 0, n-1)
heapSort(h, n)

before = time.time()
quickSort(q, 0, n-1)
T_Q = (time.time()-before)

before = time.time()
mergeSort(m, 0, n-1)
T_M = (time.time()-before)

before = time.time()
heapSort(h, n)
T_H = (time.time()-before)

print("수행 시간: ","퀵소트:",T_Q, "머지소트:",T_M, "힙소트:",T_H)

Q_C = format(Qc)
Q_S = format(Qs)
M_C = format(Mc)
M_S = format(Ms)
H_C = format(Hc)
H_S = format(Hs)
print("비교 횟수: ", "퀵소트:",Q_C, "머지소트:", M_C, "힙소트:",H_C)
print("스왑 횟수: ", "퀵소트:", Q_S, "머지소트:", M_S, "힙소트:", H_S)

assert(check_sorted(q))
assert(check_sorted(m))
assert(check_sorted(h))

