import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # StandardScaler 평균 0, 분산 1이 되게 조정
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, classification_report

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

from sklearn.model_selection import KFold

# 데이터 세트 가져오기
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values  # Feautre : 3,4번째 컬럼만 가져옴
y = dataset.iloc[:, -1].values  # Target

# Social Network Ads 데이터 기초 정보 확인하기
dataset.info()

# 총 400개의 데이터로 구성되어 있고
# 속성은 5개
# 각 속성별 값의 개수가 400개인 것을 보아 결측치없음

# 속성들을 히스토그램으로 표현
fig, ax = plt.subplots(3, 1, figsize=(12, 12))
sns.histplot(data=dataset['Age'], kde=True, color='skyblue', ax=ax[0])
sns.histplot(data=dataset['EstimatedSalary'], kde=True, color='teal', ax=ax[1])
sns.histplot(data=dataset['Purchased'], kde=True, color='gold', ax=ax[2])

plt.show()

# 히트맵으로 상관관계 나타내기
plt.figure(figsize=(5, 4))
numeric_columns = dataset.select_dtypes(include=['float64', 'int64'])
corr = numeric_columns.corr()
sns.heatmap(corr, annot=True, cmap='Spectral_r')
plt.show()

# 데이터 상단 5개 데이터 출력
dataset.head()

print('X array에서 앞 샘플 5개만 추출 :\n{}'.format(X[:5, :]))

print('y array에서 앞 샘플 5개만 추출 :\n{}'.format(y[:5]))

# 배열 크기 확인
print('X.shape : {}'.format(X.shape))
print('y.shape : {}'.format(y.shape))

# 구매 여부(Purchased) 속성의 데이터 고유값의 개수 출력
dataset['Purchased'].value_counts()

# training 데이터와 test 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=4)

print('train_test_split() 결과 :')
print('X_train.shape : {}'.format(X_train.shape))
print('X_test.shape : {}'.format(X_test.shape))
print('y_train.shape : {}'.format(y_train.shape))
print('y_test.shape : {}\n'.format(y_test.shape))
print('X_train array에서 앞 샘플 3개만 추출 :\n', format(X_train[:3, :]))

# 스케일링(feature scaling) 전 training 데이터 - Age와 EstimatedSalary
plt.figure(figsize=(10, 6))  # 사이즈
dist = sns.histplot(data=X_train, kde=True, palette='RdYlBu', multiple='stack')
dist.set_xlabel("Age")
dist.set_ylabel("Salary")
plt.show()

# # 스케일링(feature scaling) : 표준화 후 training 데이터 - Age와 EstimatedSalary
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train) # fit_transform() 으로 테스트셋에 대해 fit 과 transform 수행
# X_test = sc.transform(X_test) # transform() 으로 테스트셋에 대해서 정규화 수행
# print('fit_transform() 결과 array에서 앞 샘플 3개만 추출\n{}'.format(X_train[:3,:]))

# # 표준화 결과 시각화
# plt.figure(figsize=(10,5)) # 사이즈 지정
# dist=sns.histplot(X_train, kde=True, palette='RdYlBu', multiple='stack')
# dist.set_xlabel("Age")
# dist.set_ylabel("Estimated Salary")
# plt.show()

# 모델 선언 & 모델 학습
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# test 데이터에 대한 모델 학습 결과와 정확도 출력
y_pred = classifier.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print('정확도 : {:.3f}'.format(acc))

# Classification report 출력 - 정확도, 정밀도, 재현율, f1-score
print(classification_report(y_test, y_pred))

# 혼동행렬 만들기
plt.figure(figsize=(4, 3))  # 사이즈
ax = plt.gca()
cm = confusion_matrix(y_test, y_pred)
cm_display = ConfusionMatrixDisplay(cm)

# 혼동행렬 출력
cm_display.plot(cmap=plt.cm.Spectral, ax=ax)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Class')
plt.ylabel('Actual Class')
plt.show()

tn = cm[0, 0]
tp = cm[1, 1]
fn = cm[1, 0]
fp = cm[0, 1]

# 평가 지표 계산
precision = tp / (tp + fp)
recall = tp / (tp + fn)
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
print('정확도(accuracy) : {:.3f}'.format(acc))
print('정밀도(precision) : {:.3f}'.format(precision))
print('재현율(recall) : {:.3f}'.format(recall))
print('민감도(sensitivity) : {:.3f}'.format(sensitivity))
print('특이도(specificity) : {:.3f}'.format(specificity))

# sklearn으로 구한 평가 지표와 비교
from sklearn.metrics import precision_score, recall_score

precision_score = precision_score(y_test, y_pred)
recall_score = recall_score(y_test, y_pred)
print('===========================')
print('precision_score : {:.3f}'.format(precision_score))
print('recall_score : {:.3f}'.format(recall_score))

# # y_test (80,)
# y_test = y_test.reshape(-1,1) # (80,1)
print(X_test[0])
# 모델 학습 결과 predict_proba()로 각 클래스에 대한 확률로 반환
lr_probs = classifier.predict_proba(X_test)
print('predict_proba() 결과 shape : {}\n'.format(lr_probs.shape))
print('predict_proba() 결과 array에서 앞 샘플 5개만 추출\n{}\n'.format(lr_probs[:5, :]))
print('predict_proba() 결과 array에서 각 열마다 모든 행을 다 더한 결과\n{}'.format(lr_probs[:2, :].sum(axis=1)))

age = 30
salary = 80000
result = classifier.predict_proba([[age, salary]])
print('나이: {}\n연봉(단위:$): {}\n구매했을 확률: {:.2f}\n'.format(age, salary, result[0][1] * 100))

# AUC score
lr_auc = roc_auc_score(y_test, lr_probs[:, 1])
print('ROC AUC Score : {:.3f}'.format(lr_auc))

# ROC curve
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs[:, 1])
# roc_curve(y_true, y_score) y_score는 positive class의 확률 추정치

# ROC curve 출력
plt.plot(lr_fpr, lr_tpr, marker='.', label=f'Hold-out (AUC = {lr_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random (AUC = 0.5)')
plt.xlabel('False Positive Rate')
plt.ylabel('Ture Positive Rate')

plt.title('ROC curves')
plt.legend()
plt.show()

lr_auc = roc_auc_score(y_test, lr_probs[:, 1])
acc = accuracy_score(y_test, y_pred)

print('ROC AUC Score: {:.3f}'.format(lr_auc))
print('정확도: {:.3f}'.format(acc))

# test data에 대한 hold-out 결과 시각화
from matplotlib.colors import ListedColormap

x, y = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start=x[:, 0].min() - 1, stop=x[:, 0].max() + 1, step=0.01),
                     np.arange(start=x[:, 1].min() - 1, stop=x[:, 1].max() + 1, step=0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('skyblue', 'orange')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y)):
    plt.scatter(x[y == j, 0], x[y == j, 1],
                c=['skyblue', 'orange'][i], label=j)

plt.title('Naive Bayes (test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

X = dataset.iloc[:, [2, 3]].values  # values() : ndarray로 변환
y = dataset.iloc[:, -1].values

kf = KFold(n_splits=10)  # k=10
print('get_n_splits()로 K-Fold 검증 수 확인 : {}'.format(kf.get_n_splits(X)))
print('X.shape : {}\n'.format(X.shape))
print('X array에서 앞 샘플 5개만 추출 :\n{}'.format(X[:5, :]))

cv_accuracy = []  # fold-sets performance 저장할 리스트

# Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)  # transform() 으로 테스트셋에 대해서 정규화 수행
print('fit_transform() 결과 array에서 앞 샘플 3개만 추출\n{}'.format(X_train[:3, :]))

n_iter = 0  # 검증횟수
classifier = GaussianNB()  # 나이브 베이즈 모델

# fold별 교차검증 정확도
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    n_iter += 1

    accuracy = np.round(accuracy_score(y_test, y_pred), 3)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]

    cv_accuracy.append(accuracy)

    print('[Fold {0}]\ntraining 데이터 크기 : {1}\tvalidation 데이터 크기 : {2}\tcross-validation 정확도 : {3}'
          .format(n_iter, train_size, test_size, accuracy))
    print('-----------------------------------------------------------------------')


# 평균과 분산 구하는 함수
# 함수 연습..
def mean(lst):
    hap = 0
    for i in range(len(lst)):
        hap += lst[i]
    return hap / len(lst)


def var(lst):
    m = mean(lst)
    v = 0
    for i in range(len(lst)):
        v += (lst[i] - m) ** 2
    return v / len(lst)


print('예측 정확도 평균 : {:.3f}'.format(mean(cv_accuracy)))
print('예측 정확도 분산 : {:.3f}'.format(var(cv_accuracy)))

# AUC score
lr_probs = classifier.predict_proba(X_test)
print('predict_proba() 결과 shape : {}\n'.format(lr_probs.shape))
print('predict_proba() 결과 array에서 앞 샘플 5개만 추출\n{}\n'.format(lr_probs[:5, :]))

lr_auc = roc_auc_score(y_test, lr_probs[:, 1])
print('ROC AUC Score : {:.3f}'.format(lr_auc))

# ROC curve
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs[:, 1])
# roc_curve(y_true, y_score) y_score는 positive class의 확률 추정치

# ROC curve 출력
plt.plot(lr_fpr, lr_tpr, marker='.', c='green', label=f'10-fold (AUC = {lr_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random (AUC = 0.5)')
plt.xlabel('False Positive Rate')
plt.ylabel('Ture Positive Rate')

plt.title('ROC curves')
plt.legend()
plt.show()

# test data에 대한 k-fold 결과 시각화
from matplotlib.colors import ListedColormap
x, y = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = x[:, 0].min() - 1, stop = x[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x[:, 1].min() - 1, stop = x[:, 1].max() + 1, step = 0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('skyblue', 'orange')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y)):
    plt.scatter(x[y == j, 0], x[y == j, 1],
                c = ['skyblue', 'orange'][i], label = j)
plt.title('Naive Bayes (test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
