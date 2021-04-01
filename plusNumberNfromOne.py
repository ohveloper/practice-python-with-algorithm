# 1번째 방법 O(n)
def sum_n(n):
    s = 0
    for i in range(1, n+1):  # 1부터 시작해서 n+1 은 제외한 수까지
        s = s + i
    return s


# print(sum_n(10))
# print(sum_n(200))


# 2번째 방법 O(1)
def sum_n_once(n):
    return n * (n + 1) // 2


# print(sum_n_once(200))

# 연습문제1
# 1부터 n까지 연속한 숫자의 제곱의 합을 구하자! (for 반복문으로)

# O(n)


def sum(n):
    result = 0
    for i in range(1, n+1):
        result = result + i * i
    return result


print(sum(10))

# O(1)


def sum_O_one(n):
    return n * (n+1) * (2 * n + 1) // 6


print(sum_O_one(100))
