a = [1, 2, 3]
len(a)
print(a[-1])

# len(a) : 리스트의 길이를 구한다
# append(x) : 아이템 x 를 리스트의 맨 뒤에 추가한다
# insert(i,x) : i 번째에 x 아이템을 넣는다
# pop(i) : i 번째 아이템을 빼낸다, ()일때는 맨마지막 아이템 팝
# clear() : 리스트의 모든 자료를 지웁니다
# x in a : 어떤 자료가 a안에 있는지 확인

# 가장 큰 수 구하는 알고리즘 O(n)


def findMaxiumValue(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v


v = [123, 23, 323, 123, 234, 34534563457, 4674352344678678, 23, 234]
print(findMaxiumValue(v))


# 가장 큰수의 위치 알고리즘

def findMaxValueIdx(a):
    N = len(a)
    max_idx = 0
    for z in range(1, N):
        if a[z] > a[max_idx]:
            max_idx = z
    return max_idx


print(findMaxValueIdx(v))


# 리스트의 최소값을 리턴하는 알고리즘

def findMinValue(a):
    l = len(a)
    min_value = a[0]
    for y in range(1, l):
        if a[y] < min_value:
            min_value = a[y]
    return min_value


print(findMinValue(v))
