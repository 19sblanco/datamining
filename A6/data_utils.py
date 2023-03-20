from sklearn.datasets import load_diabetes
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

# Load entire dataset 
X, y = load_diabetes(return_X_y=True, as_frame=False)

#Make a train-test split with 20% of the data in the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

#Make 5 train-test splits of the data
#Because we chose 5 folds, each test set will consist of 20% of the data 
n_splits = 5
kf = KFold(n_splits=n_splits)
kf.get_n_splits(X)

for i, (train_index, test_index) in enumerate(kf.split(X)):
    fold_train_X = X[train_index]
    fold_train_y = y[train_index]
    fold_test_X = X[test_index]
    fold_test_y = y[test_index]