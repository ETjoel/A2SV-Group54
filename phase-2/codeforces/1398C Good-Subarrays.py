for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    for i in range(1, n):
        a[i] +=a[i-1]
    dic, res = {}, 0
    for i in range(n):
        if a[i] - (i+1) == 0:res+=1
        if a[i] - (i+1) in dic:
            res += dic[a[i] - (i+1)]
        dic[a[i] - (i+1)] = dic.get(a[i] - (i+1),0)+1
    print(res)