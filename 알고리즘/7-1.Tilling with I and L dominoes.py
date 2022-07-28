n = int(input())
DP_A = [1, 1]
DP_B = [1, 1]

for i in range(2, n+1):
    DP_A.append(DP_A[i-2] + DP_A[i-1])
    if(i>=3):
        DP_B.append(DP_B[i-1] + (DP_A[i-2])*2)
        DP_A[i] += DP_B[i-1]
    else:
        DP_B.append(DP_B[i-2] + DP_A[i-2])

print(DP_A[n])
#점화식
#An = A[n-1] + A[n-2] + B[n-1]
#Bn = B[n-1] + B[n-2]*2
#각각 그려가면서 비교해본 결과입니다.
#한 개의 블럭이 튀어나와 있을 경우는 2가지입니다. 2X4 의 보드판이 채워질 경우는 각 4가지입니다. 총 2가지니까 8가지. 즉 B[4] = 8 이라고 봤습니다.
#이런식으로 계산해서 점화식을 만들었습니다.
