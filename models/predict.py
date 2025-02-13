import numpy as np

def simple_predict(data):
    model_weights = np.array([0.5, 0.2, 0.3])  # 간단한 가중치
    prediction = np.dot(model_weights, data)  # 선형 연산
    return prediction
