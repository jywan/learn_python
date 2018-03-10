# _*_ encoding: utf-8 _*_
# 生成器实现杨辉三角
def triangles():
    n = 0
    l0 = [1]
    yield l0
    n += 1
    ln = [1, 1]
    yield ln
    while True:
        n += 1
        i = 0
        l = []
        while i <= n:
            if (i == 0 or i == n):
                l.append(1)
            else:
                l.append(ln[i-1] + ln[i])
            i += 1
        yield l
        ln = l

g = triangles()
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
