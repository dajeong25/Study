# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
# data 출처: https://www.kaggle.com/ruiromanini/mtcars 
import pandas as pd
a = pd.read_csv('data/mtcars.csv', index_col=0)

# 사용자 코딩
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
a['qsec'] = scaler.fit_transform(a[['qsec']])

ans1 = len(a[a.qsec > 0.5])
ans2 = sum(a.qsec > 0.5)

# 답안 제출 예시
print(ans1)
print(ans2)
