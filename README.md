# **ML Classification:**
# **Fixed Deposit Offer Acceptance Prediction**

This program can predict whether a specific customer will accept a term deposit offer if contacted. This is done by creating a classification machine learning model based on customer data from January 2020 to January 2024. The information generated from this model can later be used as a consideration for the marketing team in determining which customers should be offered the product.

The model creation and evaluation are carried out in the file _. Then, the model's application on new data (inference) is done in the file _.


## **Introduction**

In banking, particularly for term deposits, customers are typically contacted via phone. A term deposit is a fixed-term investment where customers store assets to earn interest. This two-way communication allows marketing teams to address questions and offer personalized deals, building trust and increasing the chance of customer conversion. However, calling is **inefficient**, requiring considerable time, effort, and cost, and customers may not always answer or may become frustrated by repeated calls. Therefore, an additional method is needed to **improve efficiency**.

**Machine learning** can identify customers most likely to accept a term deposit offer by analyzing historical data. Focusing calls on these customers can significantly **improve resource efficiency**.

## **Data Overview**

The dataset used for this project is sourced from Kaggle and consists of 17 features. The features age, job, marital, education, default, balance, housing, and loan describe the characteristics of the customer. Then, the features contact, day, month, duration, campaign, pdays, previous, and poutcome describe information regarding previous marketing communications. The target variable for prediction is y, which indicates whether the customer agrees to subscribe to a term deposit (1) or not (0).

Source: [Kaggle](https://www.kaggle.com/datasets/psvishnu/bank-direct-marketing)


Here’s a summary of the columns in the dataset:

| Key Name  | Description | Data Types |
|-----------|-------------|------------|
| age       | Customer's age | Numeric |
| job       | Customer's job type | Categorical |
| marital   | Customer's marital status | Categorical |
| education | Customer's highest level of education | Numeric |
| default   | Condition where the customer previously failed to repay a loan within the agreed period ('yes': occurred to the customer, 'no': did not occur to the customer) | Categorical |
| balance   | Average annual income received by the customer in Euros | Numeric |
| housing   | Customer's home ownership status | Categorical |
| loan      | Condition where the customer previously took an unsecured personal loan from the bank ('yes': occurred to the customer, 'no': did not occur to the customer) | Categorical |
| contact   | Type of marketing communication previously conducted with the customer | Categorical |
| day       | Date of the previous marketing communication with the customer | Numeric |
| month     | Month of the previous marketing communication with the customer | Categorical |
| duration  | Number of days of the previous marketing communication with the customer | Numeric |
| campaign  | Total number of marketing communications conducted with the customer during the current marketing campaign | Numeric |
| pdays     | Number of days since the last marketing communication with the customer from the previous campaign to the current campaign. If the value is -1, it means the customer has not been contacted in any marketing communication. | Numeric |
| previous  | Total number of marketing communications conducted with the customer during the previous marketing campaign | Numeric |
| poutcome  | Type of marketing communication used in the current campaign | Categorical |
| y         | Condition where the customer agrees to subscribe to a term deposit | Categorical |


## **Methodology**

1.	**Introduction**: Describing the problems and machine learning model, model evaluation, and methods needed to solve those problems.
2.	**Import Libraries**: Calling the required modules
3.	**Data Loading**: Loading and describing the dataset.
4.	**Exploratory Data Analysis (EDA)**: Examining the dataset to identify patterns, correlations, and trends that can guide the model development.
5.	**Feature Engineering**: Preparing the dataset so that it suitable to solve the problems.
6.	**Model Definition, Training, and Evaluation**: Preparing and training the machine learning models with the prepared dataset. Then, testing the trained model.
7.	**Model Saving**: Saving the best model so that it can be inferenced.
8.	**Conclusion**: Describing whether the model can be used to solve the problem or not.


## **Machine Learning Models Employed:**

- Logistic Regression
- K-Nearest Neighbours (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- XGBoost

## **Conclusion**

Although the train and test evaluation scores are low (indicating a poor fit), the logistic regression model provides valuable insights into customer characteristics for the marketing team. With precision scores of 0.6, this suggests that out of 100 customers willing to accept the offer, the model can correctly identify 60. However, the model alone is not sufficient to determine whether a customer will accept the offer without further verification by the marketing team.

Given that the evaluation scores for the KNN and SVC models are similar to those of the logistic regression model, there is potential for further improvement through exploration and hyperparameter tuning. One key hyperparameter to adjust is the influence of outlying data points on the decision boundary, as it is assumed that the data points have varying densities.


## **Link to Model Deployment**

You can interact with and explore the deployed model here:  
[Fixed Deposit Offer Acceptance Prediction](https://huggingface.co/spaces/mnuzulbandung/aaaa)

## **Libraries Used**

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit

## **Author**

M Nuzul  
LinkedIn: [M NUzul](https://www.linkedin.com/in/m-nuzul/)
