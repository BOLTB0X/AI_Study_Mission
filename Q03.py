import pandas as pd

idx = ["sue","Ryan","jay","jane","anna"]
col = ["round_1", "round_2","round_3","round_4","round_5"]

data = [[55,65,60,66,57], [64,77,71,79,67],[88,81,79,89,77],
        [45, 35, 30, 46, 47], [91, 96, 90, 97, 99]]

#데이터 프레임 구성
df = pd.DataFrame(data, index=idx, columns=col)

#새로운 데이터
col_round_6 = pd.Series([11, 15, 13, 17, 19], index= idx);
df["round_6"] = col_round_6
print(df)

print(df.describe().loc[["mean","max","min"]])