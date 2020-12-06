import sys
sys.setrecursionlimit(10 ** 9)

def fast_pow(a, n):
	if n == 0:
		return 1
	elif n == 1:
		return a
	elif n % 2 != 0:
		return a * fast_pow(a, n - 1)
	else:
		return fast_pow(a * a, n / 2)

a, n = map(int, input().split())
print(fast_pow(a, n))

