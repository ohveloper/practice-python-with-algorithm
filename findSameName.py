# s = set() : 집합을 만든다
# s.add(1) : {1}
# s.add(1) : {1}
# s.add(2) : {1, 2} 다른 자료만 추가된다
#
# len(s) : s 의 길이를 구한다
# s.add(x) : x 를 더한다 (위치는 랜덤)
# s.discard(x) : 집합에 자료 x가 들어있다면 삭제한다 (없으면 변화x)
# s.clear() : 집합의 모든 자료를 지운다
# x in s : 어떤 자료x 가 집합 s에 들어있는지 확인한다
# x not in s : 반대 결과

# 동명이인 찾는 알고리즘 O(n^)
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result


name1 = ["Tom", "Eddy", "Ed", "Tom"]
name2 = ["Tom", "Brown", "석영", "석영", "Eddy", "Ed", "Tom"]
print(find_same_name(name1))
print(find_same_name(name2))
