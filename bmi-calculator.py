# BMI 計算機
my_weight = input("請輸入您的體重（kg）：")
my_height = input("請輸入您的身高（cm）：")
my_weight = float(my_weight)
my_height = float(my_height)
my_bmi = my_weight / (my_height/100)**2
print("我的身高是 %.1f 公分，體重是 %.1f 公斤，BMI 為 %.2f。" % (my_height, my_weight, my_bmi))
