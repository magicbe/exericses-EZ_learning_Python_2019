# 計算五個人的 BMI
import numpy as np

heights = [173, 168, 171, 189, 179]
weights = [65.4, 59.2, 63.6, 88.4, 68.7]
heights_arr = np.array(heights)
weights_arr = np.array(weights)
bmi_arr = weights_arr / (heights_arr / 100)**2
print(bmi_arr)