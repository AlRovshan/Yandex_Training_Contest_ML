a = list(map(int,input().split()))
k = int(input())
c = 1
s = a
for _ in range(1, k):
    s_next = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            s_next[i] += s[j]
            if a[j] != a[i]:
                s_next[i] += a[i] * c
    c *= len(a)
    s = s_next

print(sum(s) / (len(a) * c))