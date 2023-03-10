"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file contains functions to answer the first research question of
a study on the mental health of tech workers. The functions create machine
learning models to predict workers' likelihood of seeking treatment and
show the correlation of factors. The models used are a Decision Tree
and a Random Forest classifier.
"""
from data_cleaning import merge_data
import plotly.figure_factory as ff
import os
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from IPython.display import Image, display
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def best_test_split(features: pd.DataFrame, labels: pd.Series) -> float:
    """
    Finds the best test split for a given dataset by testing the accuracy of
    the model trained on different test sizes from 0.1 to 0.4.

    Args:
        features (pd.DataFrame): Features of the dataset.
        labels (pd.Series): Labels of the dataset.

    Returns:
        float: Best test split value.
    """
    best_split = 0
    best_split_score = 0

    for split in np.linspace(0.1, 0.4, num=4):
        X_train, X_test, Y_train, Y_test = \
            train_test_split(features, labels, test_size=split)

        clf = DecisionTreeClassifier()
        clf.fit(X_train, Y_train)
        test_predictions = clf.predict(X_test)

        current_split_score = accuracy_score(Y_test, test_predictions)

        if current_split_score > best_split_score:
            best_split_score = current_split_score
            best_split = split

    return best_split


def best_max_depth(X_train: pd.DataFrame, X_test: pd.DataFrame,
                   Y_train: pd.Series, Y_test: pd.Series) -> int:
    """
    Finds the best maximum depth for a decision tree model by testing the
    accuracy of the model trained on different depths.

    Args:
        X_train (pd.DataFrame): Features of the training dataset.
        X_test (pd.DataFrame): Features of the testing dataset.
        Y_train (pd.Series): Labels of the training dataset.
        Y_test (pd.Series): Labels of the testing dataset.

    Returns:
        int: Best maximum depth value.
    """
    best_depth = 0
    best_depth_score = 0

    for d in range(1, 11):
        model = DecisionTreeClassifier(max_depth=d)
        model.fit(X_train, Y_train)
        test_pred = model.predict(X_test)
        current_depth_score = accuracy_score(Y_test, test_pred)

        if current_depth_score > best_depth_score and d > 1:
            best_depth_score = current_depth_score
            best_depth = d

    return best_depth


def plot_tree(model: DecisionTreeClassifier, features: pd.DataFrame,
              labels: pd.Series) -> None:
    """
    Visualizes a given decision tree model.

    Args:
        model (tree.DecisionTreeClassifier): Trained decision tree model.
        features (pd.DataFrame): Features of the dataset.
        labels (pd.Series): Labels of the dataset.
    """
    dot_data = export_graphviz(model, out_file=None,
                               feature_names=features.columns,
                               class_names=labels.unique(),
                               impurity=False,
                               filled=True, rounded=True,
                               special_characters=True)
    graphviz.Source(dot_data).render(os.path.join('output',
                                                  'tree.gv'), format='png')
    display(Image(filename=os.path.join('output', 'tree.gv.png')))


def dtc_model(features: pd.DataFrame, labels: pd.Series) -> None:
    """
    Creates the "best" Decision Tree model for the instance and
    visualizes the model.

    Args:
        df (pd.DataFrame): A pandas dataframe that contains cleaned data.

    Returns:
        None. This function does not return anything.
        It generates the "best" Decision Tree model for the given dataset
        and visualizes it using graphviz.
    """
    best_split = best_test_split(features, labels)
    X_train, X_test, Y_train, Y_test = \
        train_test_split(features, labels, test_size=best_split)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, Y_train)

    # Print accuracy
    test_predictions = clf.predict(X_test)
    print('Best Split:', format(round(best_split, 1)),
          'Test  Accuracy:', accuracy_score(Y_test, test_predictions))

    best_depth = best_max_depth(X_train, X_test, Y_train, Y_test)
    # Create an untrained model
    short_clf = DecisionTreeClassifier(max_depth=best_depth)

    # Train it on the **training set**
    short_clf.fit(X_train, Y_train)

    # Print accuracy
    test_predictions = short_clf.predict(X_test)
    print('Best Max Depth:', format(best_depth),
          'Test  Accuracy:', accuracy_score(Y_test, test_predictions))

    plot_tree(short_clf, X_train, Y_train)


def rfc_model(features: pd.DataFrame, labels: pd.Series) -> None:
    """
    Trains and evaluates a random forest classifier using the given features
    and labels, and writes the results to a text file named
    'random_forest_results.txt'. Additionally, saves the confusion matrix
    plot to a PNG image in the 'output' folder.

    Args:
        features (pd.DataFrame): A pandas dataframe of features.
        labels (pd.Series): A pandas series of labels.

    Returns:
        None. This function writes the results to a text file and saves the
        confusion matrix plot to a PNG image.
    """
    # Split the data into training and testing sets
    best_split = best_test_split(features, labels)
    X_train, X_test, Y_train, Y_test = \
        train_test_split(features, labels,
                         test_size=best_split, random_state=42)

    # Fit a random forest model with 500 trees
    rfc = RandomForestClassifier(n_estimators=500, random_state=42)
    rfc.fit(X_train, Y_train)

    # Evaluate the model on the testing data
    test_predictions = rfc.predict(X_test)
    test_accuracy = accuracy_score(Y_test, test_predictions)
    print('Test Accuracy:', test_accuracy)

    # Use cross-validation to evaluate the model
    scores = cross_val_score(rfc, features, labels, cv=5)
    cv_accuracy = np.mean(scores)
    print('Cross-Validation Accuracy:', cv_accuracy)

    # Create confusion matrix
    cm = confusion_matrix(Y_test, test_predictions)

    # Create plotly heatmap
    x = ['Predicted No Treatment', 'Predicted Treatment']
    y = ['Actual No Treatment', 'Actual Treatment']
    z = cm
    text = [[f'{value:,}' for value in row] for row in z]

    fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=text,
                                      colorscale='Blues')
    fig.update_layout(title='Random Forest Confusion Matrix')

    # Save the figure in the output folder
    fig.write_image("output/random_forest_confusion_matrix.png")

    # Print feature importances
    importances = rfc.feature_importances_
    indices = np.argsort(importances)[::-1]

    # Write the output to a text file in the 'output' directory
    with open('output/random_forest_results.txt', 'w') as f:
        # Write test accuracy to file
        f.write('Test Accuracy: ' + str(test_accuracy) + '\n\n')

        # Write cross-validation accuracy to file
        f.write('Cross-Validation Accuracy: ' + str(cv_accuracy) + '\n\n')

        # Write feature ranking to file
        f.write('Feature Ranking:\n')
        for i in range(X_train.shape[1]):
            feature_name = X_train.columns[indices[i]]
            importance = importances[indices[i]]
            rank_str = f'{i+1}. {feature_name} ({importance:.4f})\n'
            f.write(rank_str)


def research_question_1(df: pd.DataFrame) -> None:
    """
    Creates a Decision Tree and a Random Forest model to predict workers'
    likelihood of seeking treatment, and visualizes the Decision Tree model.

    Args:
        df: A pandas dataframe that contains cleaned data.

    Returns:
        None.
    """
    data = df[['Age', 'self_employed', 'family_history',
               'no_employees', 'tech_company', 'wellness_program',
               'treatment']].dropna()
    features = data.loc[:, data.columns != 'treatment']
    features = pd.get_dummies(features)
    labels = data['treatment']

    dtc_model(features, labels)
    rfc_model(features, labels)


def main():
    merged_df = merge_data()
    research_question_1(merged_df)


if __name__ == '__main__':
    main()
