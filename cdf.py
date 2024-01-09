import matplotlib.pyplot as plt
import numpy as np


# CDF 함수 정의
def cdf_Y(y):
    return np.sqrt(y)


# y 값 생성
y_values = np.linspace(0, 1, 1000)

# CDF 값 계산
cdf_values = cdf_Y(y_values)

# 그래프 그리기
plt.plot(y_values, cdf_values, label='CDF of Y')
plt.xlabel('y')
plt.ylabel('F_Y(y)')
plt.title('CDF of Y = X^2')
plt.legend()
plt.grid(True)
plt.show()
