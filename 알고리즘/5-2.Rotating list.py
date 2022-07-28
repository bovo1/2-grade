# 뼈대 코드가 없으니 입력 처리 코드도 직접 작성할 것!
# code here
def find_max(num):
    if len(num) == 1:
        return num[0]

    n = len(num)//2
    
    L1 = find_max(num[:n])
    R1 = find_max(num[n:])

    B = [L1, R1]

    if L1 > R1: M = L1
    else: M = R1
    return M

num = [int(x) for x in input().split()]
M = find_max(num)
idx_M = num.index(M)
result = len(num) - idx_M - 1

print(result)

# 질문. 본인의 알고리즘의 비교횟수를 분석한 후, Big-O로 표기해보자
# 대답  O(n)
