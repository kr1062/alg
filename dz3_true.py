def intervals(jobs):
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current = jobs[i-1]

        last_compatible = -1
        for j in range(i-1, 0, -1):
            if jobs[j-1][1] <= current[0]:
                last_compatible = j
                break
        dp[i] = dp[i-1]
        if last_compatible != -1:
            dp[i] = max(dp[i], current[2] + dp[last_compatible])
        else:
            dp[i] = max(dp[i], current[2])

    return dp[n]

jobs = [(0, 3, 3), (1, 4, 5), (3, 5, 2), (4, 7, 4), (5, 8, 6), (6, 9, 3)]
intervals(jobs)
