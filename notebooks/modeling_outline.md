# outline, Kaggle - Titanic 大綱

# 第一次上傳

### 第一步 暸解train data的資料外觀與內容

df = pd.read_csv() : 讀取資料

train.head() : 了解資料的大概情況，不要用print()會比較完整而且好看

train.shape : 資料維度

train.dtypes : 每一筆資料的儲存狀態(是integer, float, object等等)

train.info()

train.isnull().sum() : 一口氣了解有多少遺漏值

用計算幾個來衡量不太準，應該用比例來衡量(不然萬一樣本數本來就不同，直接計數去比較很容易誤判 -> 用normalize = True來改用比例去衡量)

bar_plotting()

### 第二步 train data的資料預處理 (Feature Engineering)

X 不要納入編號（PassengerId, Ticket）、姓名（Name）與遺漏值過多的變數（Cabin）
填補遺漏值 : Embarked, Age
one-hot encoding 進行類別標籤編碼轉換 : Sex, Embarked

train_sex_embarked_dummies = pd.get_dummies(train.loc[:, ["Sex", "Embarked"]])

train_sex_embarked_ohe = train_sex_embarked_dummies.values.astype(float)

透過.values先換成ndarray。為什麼要轉換過來呢?因為等等要資料水平合併、透過ndarray跑計算阿

train_sex_embarked_dummies.head()

### 第三步 分類器、模型h(x)的評估

這裡採用 : 決策樹分類器

from sklearn import tree

整理 features 跟 target

train_features = np.hstack((train.loc[:, ["Pclass", "Age", "SibSp", "Parch", "Fare"]].values, train_sex_embarked_ohe))

target = train.Survived.values

建立模型

tree_clf = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 87)

tree_clf.fit(train_features, target)

預測、模型評估

print(tree_clf.featureimportances)

print(tree_clf.score(train_features, target))

### 第四步 整理test data

對於test data也要做和train data一樣的事情 :
1- 了解資料外觀

pd.read_csv()讀取test data
test.head()了解外觀
test.shape / test.dtypes 了解test data的大概樣貌
test.isnull().sum()看test data 有沒有遺漏值，有的話等等預處理就來填補遺漏值
2- 資料預處理

(1) 填補遺漏值

Age 的遺漏值以中位數填補

age_median = test.Age.median()

test.Age = test.Age.fillna(age_median)

print(sum(test.Age.isnull())) -> 確認填補完的那一變數欄位還有沒有遺漏值

Fare 的遺漏值以平均數填補

fare_median = test.Fare.median()

test.Fare = test.Fare.fillna(fare_median)

print(sum(test.Fare.isnull())) -> 確認填補完的那一變數欄位還有沒有遺漏值

(2) one hot encoding 進行類別標籤編碼轉換

test_sex_embarked_dummies = pd.get_dummies(test.loc[:, ["Sex", "Embarked"]])

test_sex_embarked_ohe = test_sex_embarked_dummies.values.astype(float)

test_sex_embarked_dummies.head()

### 第五步 應用預測資料

整理 test_features

test_features = np.hstack((test.loc[:, ["Pclass", "Age", "SibSp", "Parch", "Fare"]].values, test_sex_embarked_ohe))

預估

predictions = tree_clf.predict(test_features)

print(predictions)

### 第六步 上傳

參考 Submission File Format 整理一下上傳檔案

PassengerId =np.array(test["PassengerId"]).astype(int)

my_solution = pd.DataFrame(predictions, PassengerId, columns = ["Survived"])

print(my_solution.head())

print(my_solution.shape)

my_solution.to_csv("my_first_solution.csv", index_label = ["PassengerId"])