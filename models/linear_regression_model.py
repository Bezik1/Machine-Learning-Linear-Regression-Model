from utils.table_operations import get_table_mult, get_table_square, table_sum

class LinearRegressionModel:
    def __init__(self, x, y, n) -> None:
        self.x = x
        self.y = y
        self.n = n
        
        self.a = self.get_slope_coefficient(x, y)
        self.b = self.get_y_intercept(x, y)
        
    def get_slope_coefficient(self, x, y):
        return ((self.n * table_sum(get_table_mult(x, y)) - table_sum(x) * table_sum(y)) / (self.n * table_sum(get_table_square(x)) - table_sum(x)**2))  
    
    def get_y_intercept(self, x, y):
        return (table_sum(y) / self.n) - self.a * (table_sum(x) / self.n)
    
    def get_r2_score(self, x, y):
        n = len(x)
        x_mean = table_sum(x) / n
        y_mean = table_sum(y) / n
        
        table_sum_squared_error = 0
        table_sum_total_error = 0
        
        for i in range(n):
            table_sum_squared_error += (y[i] - x[i])**2
            table_sum_total_error += (y[i] - y_mean)**2
        
        r_squared = 1 - (table_sum_squared_error / table_sum_total_error)
        
        return r_squared
    
    def predict(self, x):
        return self.a * x + self.b
    
    def get_prediction_y(self):
        prediction = []
        
        for el in self.x:
            prediction.append(self.predict(el))
        return prediction