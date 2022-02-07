import numpy as np

arr1 = np.random.rand(5,3) #무작위의 데이터를 가 진 5x3의 행렬
arr2 = np.random.rand(3,2) #무작위의 데이터를 가 진 3x2의 행렬

dot = arr1.dot(arr2) #행렬 곱
print(dot, dot.shape) #출력
