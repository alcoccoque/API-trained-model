from sklearn.tree import DecisionTreeClassifier


class Estimator:
    @staticmethod
    def fit(train_x, train_y):
        return DecisionTreeClassifier(cv=5).fit(train_x, train_y)

    @staticmethod
    def predict(trained, test_x):
        return trained.predict(test_x)