import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"];
data = [19, 11, 5, 97]

#Series 구성
series = pd.Series(data, index = idx)
#문제 조건
series = series[series >= 10][series <= 20]

#출력
print(series)