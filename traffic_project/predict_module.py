import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def predict_traffic(data):
    print("✅ Function loaded")   # 👈 test line

    X = np.array(range(len(data))).reshape(-1, 1)
    y = np.array(data)

    model = LinearRegression()
    model.fit(X, y)

    future = np.array(range(len(data), len(data)+10)).reshape(-1, 1)
    predictions = model.predict(future)

    plt.figure()
    plt.plot(X, y, label="Actual Traffic")
    plt.plot(future, predictions, label="Predicted Traffic")
    plt.legend()
    plt.title("Traffic Prediction")
    plt.show()

    return predictions