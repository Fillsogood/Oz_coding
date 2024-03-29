# -*- coding: utf-8 -*-
"""oz_machin_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fvGp0xNe7pasFmGYGcTBanDRd5s7_vnM

### Sikit-Learn 라이브러리
- 머신러닝을 다루는 다양한 라이브러리가 있다.
- Tensorflow, keras, Pytorch,Sikit-Learn
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install scikit-learn==1.0.2

import sklearn

# classification 분류 알고리즘을 사용해서 꽃의 종류를 구분을 하자

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

iris.data # feature 데이터
iris.target #row 데이터

# 1. 준비 되어 있는 데이터 셋을 나눕니다.
  # (1) 학습용 데이터(train_data)
  # (2) 테스트용 데이터(test_data)

# train_test_split() -> 학습용 데이터셋과 테스트용 데이터셋으로 분리하는 역할

from sklearn.model_selection import train_test_split

X_trian, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=123)

# X_trian: 학습용 피쳐 데이터, X_test: 테스트용 피쳐 데이터
# y_train: 학습용 레이블 데이터, y_test: 테스트용 레이블 데이터

y_test # 30
len(y_train) # 120

# 2. 학습을 위한 알고리즘을 불러옵니다.
from sklearn.tree import DecisionTreeClassifier # 분류 알고리즘 (supervised learning)

dt_clf = DecisionTreeClassifier(random_state=123)
dt_clf

# 3. 학습을 진행합니다. => train_data (X_trian, y_train) > 모의고사

dt_clf.fit(X_trian, y_train) # fit() - 학습을 진행

# 4. 시험을 치러갑니다. test_data(X_test, y_test) > 수능시험
# predict() - 예측하기

predict = dt_clf.predict(X_test) # 한번 풀어봐
predict

# 5. 채점을 진행합니다.
# accuracy_score()

from sklearn.metrics import accuracy_score

accuracy_score(y_test, predict) # 정답(t_test)과 실제 알고리즘(predict)이 풀이 한 정답이 일치한지 확인
# 정확도 출력

df = pd.DataFrame(data=X_test, columns=iris.feature_names)
# 수능문제지 (X_test) | aris.data 는 범위가 너무 큼

df["answer"] = y_test
df["predict"] = predict

df

iris = load_iris()
dt_clf = DecisionTreeClassifier()
dt_clf.fit(iris.data, iris.target)
pred = dt_clf.predict(iris.data)
accuracy_score(iris.target,pred)

"""## 교차 검증
- (1) K Fold 검증
- (2) Stratified 검증
- (3) cross_val_score() => 검증을 쉽게 할 수 있도록 도와주는 함수
"""

# (1) KFold
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
train_data = iris.data
train_target = iris.target

# 모델 학습 및 평가 함수 정의
def train_and_evaluate(train_index, test_index, model, train_data, train_target):
  # 학습 및 검증 데이터 분리
  X_train, X_test = train_data[train_index], train_data[test_index]
  y_train, y_test = train_target[train_index], train_target[test_index]

  # 모델 학습 및 예측
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)

  # 정확도 계산
  accuracy = accuracy_score(y_test, predictions)
  return accuracy, X_train.shape[0], X_test.shape[0], test_index

# KFold 교차 검증 설정
kfold = KFold(n_splits=5)
cv_accuracy = []
dt_clf = DecisionTreeClassifier()

# KFold 교차 검증 수행
for fold, (train_index, test_index) in enumerate(kfold.split(train_data), 1):
  accuracy, train_size, test_size, test_idx = train_and_evaluate(
      train_index, test_index, dt_clf, train_data, train_target
  )
  cv_accuracy.append(accuracy)


  print(f"{fold}번째 트레이닝")
  print(f"검증 정확도: {accuracy}, 학습 데이터 크기: {train_size}, 검증 데이터 크기: {test_size}")
  print(f"검증 데이터 셋 인덱스 값: {test_idx}")
  print(f"===" * 10)

# 최종 정확도 평균 출력
print("최종 정확도 평균 값: ", np.mean(cv_accuracy))

# (2) Stratified 검증
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# iris 데이터 셋 로드

iris = load_iris()
features = iris.data
label = iris.target

# 모델 초기화
dt_clf = DecisionTreeClassifier(random_state=156)

# Stratified KFold 교차 검증 설정
skfold = StratifiedKFold(n_splits=3)
cv_accuracy = []

# Stratified KFold 교차 검증 수행

for fold, (train_index, test_index) in enumerate(skfold.split(features, label), 1):
  accuracy, train_size, test_size, test_idx = train_and_evaluate(
      train_index, test_index, dt_clf, features, label
  )
  cv_accuracy.append(accuracy)

  # 출력 메세지 변경
  print(f"{fold}번째 트레이닝")
  print(f"검증 정확도: {accuracy}, 학습 데이터 크기: {train_size}, 검증 데이터 크기: {test_size}")
  print(f"검증 데이터 셋 인덱스 값: {test_idx}")
  print("===" * 10)

# 교차 검증 별 정확도 및 평균 정확도 계산
print("\n최종 정확도 평균 값:", np.mean(cv_accuracy))

#  cross_val_score()
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
import numpy as np

iris_data = load_iris()
dt_clf = DecisionTreeClassifier(random_state=156)

data = iris_data.data
label = iris_data.target

scores = cross_val_score(dt_clf, data, label, scoring="accuracy", cv=5) #  scoring= 평가지표, cv=교차 검증 폴드 수

print("교차 검증 별 정확도: ", np.round(scores, 5))
print("평균 검증 정확도: ", np.round(np.mean(scores), 5))

"""### 데이터 인코딩
- (1) Label Encoding
- (2) OneHot Encoding
- (3) GetDeummies - pd의 df를 활용하는 방법
"""

from sklearn.preprocessing import LabelEncoder

items=['강남구','서초구','송파구','노원구','마포구','마포구','용산구','용산구']

# LabelEncoder를 객체로 생성한 후 , fit() 과 transform() 으로 label 인코딩 수행.
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
print('인코딩 변환값:',labels) # 문자열 값 -> 숫자형 값으로 변경 (Label Encoding)

from sklearn.preprocessing import OneHotEncoder
import numpy as np

items=['강남구','서초구','송파구','노원구','마포구','마포구','용산구','용산구']

# 2차원 ndarray로 변환합니다.
# reshape() 함수의 첫 번째 인자로 -1을 주면 해당 차원의 크기를 자동으로 계산하여 맞춰줍니다.
# 두 번째 인자로 1을 주면 열의 크기를 1로 지정하여 결과적으로 1개의 열로 이루어진 2차원 배열을 생성합니다.
# 이렇게 2차원 배열로 변환된 데이터는 머신 러닝 모델에 입력으로 사용하기에 적합한 형태가 됩니다.
# 머신 러닝 모델은 비력으로 2차원 배열을 기대하므로, 데이터를 이와 같은 형태로 변환하여 모델에 사용해야 합니다.
items = np.array(items).reshape(-1,1)

# 원-핫 인코딩을 적용합니다.
oh_encoder = OneHotEncoder()
oh_encoder.fit(items)
oh_labels = oh_encoder.transform(items)

# OneHotEncoder로 변환한 결과는 희소행렬(Saprse Matrix)이므로 toarray()를 이용하여 밀집 행렬(Dense Matrix)로 변환
print('원-핫 인코딩 데이터')
print(oh_labels.toarray())
print('원-핫 인코딩 데이터 차원')
print(oh_labels.shape)

# df.get_dummies()
import pandas as pd

df = pd.DataFrame({'item':['강남구','서초구','송파구','노원구','마포구','마포구','용산구','용산구']})

pd.get_dummies(df)

# 데이터 로드
import pandas as pd

df_train = pd.read_csv("train.csv")
df_train.head(3)

df_test = pd.read_csv("test.csv")
df_test.head(3)

#  EDA (Exploratory Data Analysis)
print(df_train.columns)
print(df_test.columns)

print(df_train.shape)
print(df_test.shape)

print(df_train.info)
print(df_test.info)

#  null 데이터 갯수 체크
print(df_train.isna().sum())
print(df_test.isna().sum())

# 어떤 컬럼을 살리고, 어떤 컬럼을 지울것인가? => 시각화를 통해서 진행
import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(column_name):
    survived = df_train[df_train['Survived'] == 1][column_name].value_counts()
    dead =df_train[df_train['Survived'] == 0][column_name].value_counts()

    df_merged = pd.DataFrame({'Survived':survived,'Dead':dead})
    df_merged.plot(kind='bar',stacked=True,figsize=(12,8))

bar_chart('Parch')

bar_chart('Embarked')

# 가장 많은 요금을 낸 상위 10명의 생존율은 어떻게 될까요?
df_train.sort_values(by='Fare',ascending=False).head(10)['Survived'].value_counts()
df_train.sort_values(by='Fare',ascending=False).tail(10)['Survived'].value_counts()

df_train[["Name","Survived"]]

# 이름으로 값들 추려서 확인
train_test_data = [df_train, df_test]

for data in train_test_data:
  data["Name"] = data["Name"].str.extract(" ([A-Za-z]+)\. ") # extract 추출하기

df_train["Name"]
# df_train["Name"].value_counts()

# 문자열 -> 숫자형 데이터로 변경
name_mapping = {
    "Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3, "Dr": 4, "Rev": 5
}

for data in train_test_data:
  data["Name"] = data["Name"].map(name_mapping)

df_train["Name"].value_counts()

bar_chart("Name")

# Sex
df_train["Sex"] = df_train["Sex"].replace({"male":0, "female":1})
df_test["Sex"] = df_test["Sex"].replace({"male":0, "female":1})

df_train["Sex"].value_counts()
df_test["Sex"].value_counts()

# Age
df_train["Age"].isna().sum()

df_train.groupby("Name")["Age"].mean()

df_train["Age"].fillna(df_train.groupby("Name")["Age"].transform("mean"), inplace=True)
df_test["Age"].fillna(df_test.groupby("Name")["Age"].transform("mean"), inplace=True)

df_train["Age"].isna().sum()

df_test["Age"].isna().sum()

df_test["Age"].fillna(df_test["Age"].mean(), inplace=True) # Nan인 부분을 변경
df_test["Age"].isna().sum() # null 데이터 갯수 확인

# Age

df_train["Age"].value_counts()

df_train["Age"].isna().sum() # null 데이터 갯수 확인

import numpy as np

# age_bins = [0, 16, 32, np.inf] #inf: infinite
age_bins = [0, 16, 32, 50, 100]
age_labels = [0, 1, 2, 3]

for data in train_test_data:
  data["Age"] = pd.cut(data["Age"], bins=age_bins, labels=age_labels)

df_train["Age"].value_counts()

# SibSp, Parch
df_train["Family"] = df_train["SibSp"] + df_train["Parch"] + 1
df_test["Family"] = df_train["SibSp"] + df_train["Parch"] + 1

# 위 아래 둘 중 하나 사용 하기

for data in train_test_data:
  data["Family"] = data["SibSp"] + data["Parch"] + 1

df_train["Family"].value_counts()

# Fare
df_train["Fare"].isna().sum() # null 데이터 갯수 체크

fare_bins = [0, 20, 100, 1000]
fare_labels = [0, 1, 2]

for test in train_test_data:
  data["Fare"] = pd.cut(data["Fare"], bins=fare_bins, labels=fare_labels)

df_train["Fare"].value_counts()

# Embarked
df_train["Embarked"] = df_train["Embarked"].replace({"S":0, "C":1, "Q":2})
df_test["Embarked"] = df_train["Embarked"].replace({"S":0, "C":1, "Q":2})

df_test["Age"].fillna(0, inplace=True)
df_test["Age"].isna().sum()

df_train["Embarked"].value_counts()

df_train["Embarked"].fillna(0, inplace=True)
df_test["Embarked"].fillna(0, inplace=True)

df_train["Embarked"].isna().sum()
df_test["Embarked"].isna().sum()

df_train # 데이터 목록 확인용 (생략가능)

# drop_train_cols = ["Embarked", "SibSp", "Parch", "Ticket", "Cabin"]
drop_train_cols = ["PassengerId", "SibSp", "Parch", "Ticket", "Cabin"]

df_train_final = df_train.drop(drop_train_cols, axis=1)
df_train_final

df_test # 데이터 목록 확인용 (생략가능)

drop_test_cols = ["SibSp", "Parch", "Ticket", "Cabin"]

df_test_final = df_test.drop(drop_test_cols, axis=1)
df_test_final

# 모델링
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

features = df_train_final.drop("Survived", axis=1)
labels = df_train_final["Survived"]

df_train_final.fillna(0, inplace=True)
df_train_final.isna().sum()

# kfold
kfold = KFold(n_splits=10, shuffle=True, random_state=123)
dt_clf = DecisionTreeClassifier()
scores = cross_val_score(dt_clf, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

# KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

# RandomForestClassifier
rf = RandomForestClassifier(n_estimators=5)
scores = cross_val_score(rf, features, labels, cv=kfold, scoring="accuracy")

# scores
print(np.mean(scores)*100)# RandomForestClassifier
rf = RandomForestClassifier(n_estimators=5)
scores = cross_val_score(rf, features, labels, cv=kfold, scoring="accuracy")

# scores
print(np.mean(scores)*100)

# GaussianNB
gb = GaussianNB()
scores = cross_val_score(gb, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

# SVC
svc = SVC()
scores = cross_val_score(svc, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

df_train_final

df_test_final

# SVC 알고리즘을 사용해서 최종 결과 값 도출
svc = SVC()
scores = cross_val_score(svc, features, labels, cv=kfold, scoring="accuracy")

# 수능 문제는?
test_data = df_test_final.drop("PassengerId", axis=1)
test_data

pred = svc.predict(test_data)
pred

df_final_submit = pd.DataFrame({
    "PassengerId": df_test_final["PassengerId"],
    "Survived": pred
    })

df_final_submit.set_index("PassengerId", inplace=True)

df_final_submit.to_csv("submission.csv")