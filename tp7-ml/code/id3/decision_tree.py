import numpy as np
import pandas as pd


def entropy(y):

    # Gets an array of the counts for each value
    values, counts = np.unique(y, return_counts=True)

    # Calculates the probabilities
    probs = counts / len(y)

    # Applies the formula over the arrays and returns
    return -np.sum(probs * np.log2(probs))

# Function to calculate information gain
def information_gain(X, y, attribute):
    total_entropy = entropy(y)
    
    # Split dataset by unique values of the attribute
    values, counts = np.unique(X[attribute], return_counts=True)
    
    weighted_entropy = 0
    for value, count in zip(values, counts):
        subset = y[X[attribute] == value]
        weighted_entropy += (count / len(y)) * entropy(subset)
    
    return total_entropy - weighted_entropy

# Function to build the decision tree recursively, where X holds the predictors
# and Y the predicted attribute
def build_tree(X, y, features):
    if len(np.unique(y)) == 1:
        return np.unique(y)[0]  # Leaf node with class label
    
    # Returns majority class
    if len(features) == 0:
        return np.unique(y)[np.argmax(np.unique(y, return_counts=True)[1])]  

    # Calculate information gain for each feature
    gains = [information_gain(X, y, feature) for feature in features]
    
    # Select feature with the highest information gain
    best_feature = features[np.argmax(gains)]
    
    # Create the tree with a decision node
    tree = {best_feature: {}}
    
    # Remove the selected feature from the list
    features = [f for f in features if f != best_feature]
    
    # Split the data and recurse for each subset
    for value in np.unique(X[best_feature]):
        subset_X = X[X[best_feature] == value]
        subset_y = y[X[best_feature] == value]
        subtree = build_tree(subset_X, subset_y, features)
        tree[best_feature][value] = subtree
    
    return tree

# Function to predict the class of a new observation using the decision tree
def predict_discrete(tree, observation):
    # Loop through each node in the tree
    for feature, branches in tree.items():
        # Get the value of the current feature in the observation
        value = observation[feature]
        
        # Move to the next branch based on the feature's value
        if value in branches:
            subtree = branches[value]
        else:
            print(f"Can't predict with undefined tree value: \"{value}\", of feature \"{feature}\"")
            return None

        # Traverses recurse        
        if isinstance(subtree, dict):
            return predict_discrete(subtree, observation)
        
        # Leaf node
        else:
            return subtree 



if __name__ == "__main__":
    
    # Load the dataset
    df = pd.read_csv('tennis_data.csv')
    print(df.head())
    
    # Define features (X) and target (y)
    X = df[['outlook', 'temp', 'humidity', 'windy']]
    y = df['play']
    
    # Build the decision tree
    tree = build_tree(X, y, list(X.columns))
    
    print("Decision Tree:", tree)
    
    print("Testing tree over train data...")
    
    # Get the number of observations
    observation_count = len(df)
    predicted_successfully_count = 0
    
    # Loop through each observation (row) in the dataset
    for i in range(observation_count):
        # Create a dictionary for the observation
        observation = {
            'outlook': df.iloc[i]['outlook'],
            'temperature': df.iloc[i]['temp'],
            'humidity': df.iloc[i]['humidity'],
            'windy': df.iloc[i]['windy']
        }
        
        # Get the actual label for the current row
        y_true = df.iloc[i]['play']
        
        # Predict the label using the decision tree
        y_prediction = predict_discrete(tree, observation)
        
        # Count the correctly predicted labels
        if y_true == y_prediction:
            predicted_successfully_count += 1
    
    # Calculate accuracy
    accuracy = predicted_successfully_count / observation_count
    print(f"Accuracy: {accuracy}")