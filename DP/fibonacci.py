"""
Some Dynamic Programming Algorithms
"""

# possible of achieving log n but this DP algo is O(n)
def fibonacci(n, memo):
	if n in memo:
		return memo[n]
	if n==0:
		memo[n] = 0
		return memo[n]
	if n==1 or n==2:
		memo[n] = 1
		return memo[n]
	f = fibonacci((n-1), memo) + fibonacci((n-2), memo)
	memo[n] = f
	return memo[n]

print(fibonacci(100, {}))

