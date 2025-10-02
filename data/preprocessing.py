import pandas as pd
from sklearn.preprocessing import StandardScaler
import sys

def create_processed_csv(input_file, output_file):
    '''
    Preprocesses the input CSV file and saves the processed data to the output CSV file.
    Steps:
    1. Convert the target variable to binary: Obese (1) vs Not Obese (0)
    2. Identify binary and categorical columns.
    3. Split the dataframe into three parts: binary, categorical, and numerical.
    4. One-hot encode categorical variables.
    5. Scale numerical features.
    6. Combine all parts back into a single dataframe and save to CSV.
    7. Print a confirmation message.
    '''
    # Convert CSV to pandas dataframe
    df = pd.read_csv(input_file)

    # Convert the target variable to binary: Obese (1) vs Not Obese (0)
    obese_values = ['Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III']
    df['Obese'] = df['0be1dad'].apply(lambda x: 1 if x in obese_values else 0)
    df = df.drop(columns=['0be1dad', 'id'])

    # Identify binary and categorical columns
    binary_columns = []
    categorical_columns = []
    for column in df.columns:
        if df[column].nunique() == 2 and df[column].dtype == 'int64':
            binary_columns.append(column)
        elif df[column].dtype == 'object':
            categorical_columns.append(column)

    # Split the dataframe into three parts
    df_binary = df[binary_columns].copy()
    df_categorical = df[categorical_columns].copy()
    df_need_scaling = df.drop(columns=binary_columns + categorical_columns)

    # One-hot encode categorical variables
    df_categorical_onehot = pd.get_dummies(df_categorical, drop_first=False, dtype=int)

    # Scale numerical features
    scaler = StandardScaler()
    df_need_scaling_scaled = pd.DataFrame(scaler.fit_transform(df_need_scaling), columns=df_need_scaling.columns)

    # Combine all parts back into a single dataframe and saves to CSV
    df_prep = pd.concat([df_binary, df_categorical_onehot, df_need_scaling_scaled], axis=1)
    df_prep.to_csv(output_file, index=False)
    print(f'{str(output_file).split("/")[-1]} has been saved to the {str(output_file).split("/")[-2]} folder')