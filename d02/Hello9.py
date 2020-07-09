# 撰寫一個 BMI 系統
# 可以輸入人名, 身高, 體重
# 系統會算出 BMI 的結果與是否正常, 過高,過低
# 資料呈現 : 小明的身高是 178cm 體重是68kg  BMI 計算結果為 29.76 (5/4正常)
#資料呈現 :___的身高是___cm是體重是 BMI 計算結果為
print('BMI 系統')
name = input('請輸入姓名')
h = float(input('請輸入身高(cm): '))
w = float(input('請輸入體重(kg): '))
bmi = w / ((h/100)**2)
result = '正常' if 18 < bmi <=23 else '過高' if bmi > 23 else '過低'
print('%s的身高是 %5.1f cm 體重是 %f kg BMI 計算結果為 %5.2f (%s)' %
      (name, h, bmi, result))

