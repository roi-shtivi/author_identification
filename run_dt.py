import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import tree, ensemble
# import graphviz

# 'min_weight_fraction_leaf',
# 'class_weight',
# 'min_samples_split',
# 'max_depth',
# 'criterion',
# 'min_samples_leaf',
# 'random_state',
# 'max_features',
# 'min_impurity_split',
# 'max_leaf_nodes',
# 'splitter',
# 'presort'


parameters = {
    'max_depth': [1, 2, 3, 4, 5],
    'max_features': [1, 2, 3, 4]
}


def run(test_ratio, data, split_by_book=False, repeat=False):
    print("dt")
    run_count = 0
    score_sum = 0
    if repeat:
        num_of_runs = 100
    else:
        num_of_runs = 1
    while run_count < num_of_runs:
        print("run ", run_count)
        if split_by_book:
            training_data, test_data = calculate_features.split_train_test(data)
            X_train = training_data[:, 0]
            y_train = training_data[:, 1]
            X_test = test_data[:, 0]
            y_test = test_data[:, 1]
        else:
            X = data[:, 0]
            y = data[:, 1]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio)
        # if you want to play with it.
        # clf = GridSearchCV(tree.DecisionTreeClassifier(criterion='entropy'), parameters)
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_features=4, max_depth=4)
        # train
        clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
        # test
        score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))
        score_sum += score
        run_count += 1
        print("score = ", score)
    print("score average = ", score_sum / num_of_runs)
    return clf, score_sum

    # print the tree
    # dot_data = tree.export_graphviz(clf.best_estimator_, out_file=None)
    # graph = graphviz.Source(dot_data)
    # graph.render("dt")