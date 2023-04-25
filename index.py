import matplotlib.pyplot as plt
import numpy as np
from models.linear_regression_model import LinearRegressionModel

x = [3, 3, 2, 4, 1, 5, 6]
y = [20, 25, 20, 30, 10, 40, 55]

regression = LinearRegressionModel(x, y, len(x))
y_pred = regression.get_prediction_y()
r2 = regression.get_r2_score(y, y_pred)
print(regression.a, regression.b)

fig, ax = plt.subplots()
ax.scatter(x, y, color='black')
ax.plot(x, y_pred, color='blue', linewidth=3)
ax.set_title('Dopasowanie modelu')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.text(0.05, 0.95, f'R^2 = {r2:.3f}', transform=ax.transAxes, fontsize=14, va='top')
plt.show()