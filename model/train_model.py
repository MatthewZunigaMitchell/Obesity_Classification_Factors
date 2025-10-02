# import necessary libraries
import sklearn
import pickle
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score

def train_model(input_file, output_file):
    '''
    Trains a Logistic Regression model on the preprocessed data.
    Steps:
    1. Load the preprocessed CSV file.
    2. Split the data into training and testing sets.
    3. Create and train a Logistic Regression model.
    4. Print model scores.
    5. Check if the model meets accuracy and recall requirements, and save the model if it does.
    6. Create a feature importance dataframe and save it to CSV.
    7. Print a confirmation message.
    '''
    # Load the preprocessed CSV file
    df_prep = pd.read_csv(input_file)

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        df_prep.drop(columns=['Obese']),
        df_prep['Obese'],
        test_size=0.15,
        random_state=42,
        stratify=df_prep['Obese']
    )

    # Create and train a Logisitc Regression model
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(x_train, y_train)

    # Prints model scores
    print("Training accuracy:", model.score(x_train, y_train))
    print("Testing accuracy:", model.score(x_test, y_test))
    print("model recall:", sklearn.metrics.recall_score(y_test, model.predict(x_test)))

    # Prints model requirment results and saves the model if it passes testing
    if model.score(x_test, y_test) >= .95 and recall_score(y_test, model.predict(x_test)) >= .95:
        print("Model meets the accuracy and recall requirements.\n")
        filename = 'model/obese_logistic_regression_model.pkl'
        with open(filename, 'wb') as file:
            pickle.dump(model, file)
            file.close()
    else:
        print("Model does not meet the necessary requirements.\n")

    # Creates feature_importance dataframe
    features = x_train.columns
    coefficients = model.coef_[0]
    feature_importance = pd.DataFrame({'Feature': features, 'Coefficient': coefficients})
    feature_importance['Absolute_Coefficient'] = np.abs(feature_importance['Coefficient'])

    # Creates feature_importance CSV
    feature_importance.to_csv(output_file, index=False)
    print(f'{str(output_file).split("/")[-1]} has been saved to the {str(output_file).split("/")[-2]} folder')

