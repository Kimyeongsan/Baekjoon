import sys
INF = float('inf')
OUT, IN, BOTH = 0, 1, 2

def f(dp, outer, inner):
    for i in range(1, N):
        outer_squad = 1 if outer[i-1] + outer[i] <= W else 2
        inner_squad = 1 if inner[i-1] + inner[i] <= W else 2
        verti_squad = 1 if outer[i] + inner[i] <= W else 2
        
        dp[i][OUT] = min(dp[i-1][IN] + outer_squad, dp[i-1][BOTH] + 1)
        dp[i][IN] = min(dp[i-1][OUT] + inner_squad, dp[i-1][BOTH] + 1)
        dp[i][BOTH] = min(dp[i-1][BOTH] + verti_squad, \
                          dp[i-2][BOTH] + outer_squad + inner_squad, \
                          dp[i-1][IN] + outer_squad + 1, \
                          dp[i-1][OUT] + inner_squad + 1)

def case1():
    dp = [[0]*3 for _ in range(N)]
    dp[0][OUT] = dp[0][IN] = 1
    dp[0][BOTH] = 1 if outer[0] + inner[0] <= W else 2
    outer_cpy, inner_cpy = outer[:], inner[:]
    f(dp, outer_cpy, inner_cpy)
    return dp[N-1][BOTH]
    
def case2():
    if outer[0] + outer[N-1] > W:
        return INF
    dp = [[0]*3 for _ in range(N)]
    dp[0][OUT] = dp[0][IN] = 1
    dp[0][BOTH] = 2
    outer_cpy, inner_cpy = outer[:], inner[:]
    outer_cpy[0] = outer_cpy[N-1] = INF
    f(dp, outer_cpy, inner_cpy)
    return dp[N-1][IN]

def case3():
    if inner[0] + inner[N-1] > W:
        return INF
    dp = [[0]*3 for _ in range(N)]
    dp[0][OUT] = dp[0][IN] = 1
    dp[0][BOTH] = 2
    outer_cpy, inner_cpy = outer[:], inner[:]
    inner_cpy[0] = inner_cpy[N-1] = INF
    f(dp, outer_cpy, inner_cpy)
    return dp[N-1][OUT]

def case4():
    if outer[0] + outer[N-1] > W:
        return INF
    if inner[0] + inner[N-1] > W:
        return INF
    dp = [[0]*3 for _ in range(N)]
    dp[0][OUT] = dp[0][IN] = 1
    dp[0][BOTH] = 2
    outer_cpy, inner_cpy = outer[:], inner[:]
    outer_cpy[0] = outer_cpy[N-1] = INF
    inner_cpy[0] = inner_cpy[N-1] = INF
    f(dp, outer_cpy, inner_cpy)
    return dp[N-2][BOTH]

T = int(sys.stdin.readline())
for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    outer = list(map(int, sys.stdin.readline().split()))
    inner = list(map(int, sys.stdin.readline().split()))
    if N == 1:
        print(1 if outer[0] + inner[0] <= W else 2)
        continue

    ans1 = case1()
    ans2 = case2()
    ans3 = case3()
    ans4 = case4()
    print(min(ans1, ans2, ans3, ans4))
