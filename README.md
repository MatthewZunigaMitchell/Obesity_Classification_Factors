# Obesity_Classification_Factors
    Last updated: 10/02/2025

## Authors
1. Matthew Zuniga-Mitchell

## Purpose
The purpose of this project is to identify the top three leading features in an obesity classification (1).   
This information and the produced model can than be used by everyday individuals to gain a preliminary obesity classification, aid in deciding next steps, and understand their part in the obesity epidemic. Additonally this projects model and findings can be utilized by medical proffessionals in guiding further research into the disease.

## Scope
The scope of the project includes collecting, cleaning, encoding, and correlating the data provided by MIT and made available on Kaggle. It also includes model training, testing, and model coefficient comparisons. All the provided data will be utilized except for the 'id' column.


Not included in the scope of this project is a real-time classification utility or other methods of direct use. This project will only provide a model, not a method of making it easily accessiable by the public. 

## Deliverables
The project deliverables are as follows:
1. Age distribution graph: Histogram of age frequencies in the dataset
2. Height distribution graph: Histogram of height frequencies in the dataset
3. A preprocessed data set: This data set will be ready for Logisitc Regression model use
4. A trained model: This Logisitc Regression model will need to pass metic requirements
5. Feature importance on absolute coefficients graph: Barchart of all cloumns absolute coefficients sorted.
6. Feature importance on coefficients graph: Barchart of all columns coefficients sorted.
7. Obesity correlation graph: Barchat with feature correlation with obesity sorted. 

## Hypothiesis
This project aims to identify the factors the contribute the most to obesity classifications. I hypothesize that the top three factors that contribute the most to an obesity classification are age, height, and frequency of physical activity. To test this, I will be creating a Logisitc Regression model and examining the variable coefficients. For the model to be considered complete, it must meet the appropriate accuracy and recall scores. 

## Model and Model Metrics
Type of model: Supervised classification model  
Algorithm used: Logistic Regression algorithm  
Metrics to assess performance: 
    1. Recall
    2. Accuracy

Benchmark for success:
    1. Model produces a recall score greater than or equal to 0.95 or 95%
    2. Model produces an accuracy score greater than or equal to 0.95 or 95%

Metic reasoning:  
Since this data relates to human health and could be used to get a preliminary obesity classification, the results should correctly classify as many individuals as possible and correctly classify obesity when seen.
    1. Recall: 
        A. A measure of how many of the truly positive cases the model correctly classifies.
    2. Accuracy
        B. A measure of how many records were correctly classified in the model.

## Project Summary
This project aimed to identify the leading three features in classifying a record as obese. After producing a Logisitc Regression model that satisfied the recall and accuracy requirments, the model's coefficients were pulled and examined. The top three positive coefficents are:
1. Weight: Coefficient value of 9.25
2. FAVC: Coefficient value of 1.17
3. family_history_with_overweight: Coefficient value of 0.98

These results did not support the hypothesis that the top three factors are age, height, and frequency of physical activity. Even though the hypothesis was not supported, I consider this projecy a success. I was able produce a model that can be used by others to classify obesity and I identified the features that contribute the most to an obesity classification. These result can be used by others to aid in their research, obtain a priliminary obesity classification, and understand their part in the obesity epidemic. 

## Dataset Information
Name: Obesity Risk Dataset    
Origin: Kaggle  
Link: https://www.kaggle.com/datasets/jpkochar/obesity-risk-dataset  
License: MIT (No restrictions)  
Data set description:
This data is comprised of 20 thousand rows and 17 columns. These columns are:
1. Gender
2. Age
3. Height
4. Weight
5. Family_history_with_overweight
6. FAVC (Frequent consumption of high-caloric food)
7. FCVC (Frequency of consumption of vegetables)
8. NCP (Number of main meals)
9. CAEC (Consumption of food between meals)
10. SMOKE
11. CH2O (Daily water consumption)
12. SCC (Caloric beverages consumption)
13. FAF (Physical activity frequency)
14. TUE (Time spent using technological devices)
15. CALC (Consumption of alcohol)
16. MTRANS (Mode of transportation)
17. 0be1dad (Target variable representing obesity level)