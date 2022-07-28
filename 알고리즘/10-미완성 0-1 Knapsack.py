import copy

def costsort1(ce):
    m = 0
    m = max(ce)
    for i in range(len(ce)):
        if ce[i] == m:
            index = i
            break
    return index, m

def costsort2():
    fsn = copy.deepcopy(sn)
    fvn = copy.deepcopy(vn)
    cost_eff = []
    for i in range(len(fsn)):
        cost_eff.append(fvn[i] / fsn[i])
    #print(cost_eff)
    
    new_cost_eff = [0] * len(fsn)
    new_sn = [0] * len(fsn)
    new_vn = [0] * len(fsn)
    for j in range(len(fsn)):
        index, m = costsort1(cost_eff)
        new_cost_eff[j] = m
        new_sn[j] = fsn[index]
        fsn.pop(index)
        new_vn[j] = fvn[index]
        fvn.pop(index)
        cost_eff.pop(index)
    return new_sn, new_vn, new_cost_eff

def frac_knapsack(i, size):  
    #i가 시작 인덱스라면?
    ps = 0
    pv = 0
    for i in range(n-i):
        if ps + nsn[i] <= size:
            ps += nsn[i]
            pv += nvn[i]
            #print("1 ","nsn= ",nsn[i], "nvn= ", nvn[i], "size= ", size, ps, pv)
        else:
            #print("2-1", "size-ps=", size-ps, "pv=", pv, "nce[i]=", nce[i], "nce[i]*(size-ps)=", nce[i]*(size-ps))
            pv += nce[i]*(size - ps)
            ps = size
            #print("2-2", "nsn= ",nsn[i], "nvn= ", nvn[i], "size= ", size, ps, pv)
    return pv
        



def knapsack(i, size):
    global s, p, M, x, dmdkdkr
    if i > n or size <= 0:
        z = 0
        #print(x)
        for k in range(len(x)):
            if x[k] == 1:
                z += nvn[k]
        dmdkdkr.append(z)

        return dmdkdkr

    for j in range(i):
        if x[j] == 1:
            p += nvn[j]
            s += nsn[j]

    # x[i] = 1을 따라가야하는지 결정
    if nsn[i] <= size:
        M = p
        B = frac_knapsack(i+1, size-nsn[i])
        if p + nvn[i] + B > M:
            # Update MP
            if p + nvn[i] > M:
                M = p + nvn[i]
            x[i] = 1
            knapsack(i+1, size-(s + nsn[i]))
    x[i] = 0
    B = frac_knapsack(i+1, size)
    if p + B > M:
        x[i] = 0
        knapsack(i+1, size)


p = 0
s = 0
M = 0
k = int(input())
n = int(input())
x = [0]*n
sn = list(map(int, input().split()))
vn = list(map(int, input().split()))
dmdkdkr = []

#print(k)
#print(n)
#print(sn)
#print(vn)

nsn, nvn, nce = costsort2()

#print(nsn, nvn, nce)

#print(frac_knapsack(0, k))


knapsack(0, k)
print(max(dmdkdkr))
