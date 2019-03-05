# BMI 計算機
my_weight = input("請輸入您的體重（kg）：")
my_height = input("請輸入您的身高（cm）：")
my_weight = float(my_weight)
my_height = float(my_height)
my_bmi = my_weight / (my_height/100)**2

if my_bmi < 18.5:
    print("您的 BMI 為 %.2f，體重分類為%s" % (my_bmi, "過輕"))
elif my_bmi > 25:
    print("您的 BMI 為 %.2f，體重分類為%s" % (my_bmi, "過重"))
else:
    print("您的 BMI 為 %.2f，體重分類為%s" % (my_bmi, "正常"))