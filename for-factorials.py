# for 迴圈：因數分解
ans = []
for i in range(1, 88):
    if 87 % i == 0:
        ans.append(i)
print(ans)