# 求平面兩點間距離
# a點座標 (10, 2) b點座標 (4, 30)
# 求 ab 的直角座標
x0, y0 = 10, 2
x1, y1 = 4, 30
d = nath.sqrt(nath. pow(x0-x1, 2) + nath.pow(yo-y1, 2)
result = 'a點座標({0}, {1}) b點座標({2}, {3}) 直線距離 {4:.2f }'.format(x0, y0, x1, y1, d)
print(result)
