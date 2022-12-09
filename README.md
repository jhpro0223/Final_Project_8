# Final_Project_8
# Credit Risk Analysis

## Background
A credit history dataset of the customers from a financial institution has been given to this group by a ckient . Agenda is to predict for possible credit defaulters upfront and help the financial institutions to take steps accordingly. 
The client has made it primary that they want to evaluate the customers based on their "loan status" as a potential risk parameter.
Each week the progress of the project is provide to the Supervisor and this section covers the machine learning module of the project.

## Database
The database is a relational database. PostgreSQL has been used for the database and deployed in Amazon RDS.

The original loan data is sourced from Kaggle Credit Risk Analytics case.
[https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset](https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset "loan data source")

The data has been further enriched by joining US census bureau data ([https://data.census.gov](https://data.census.gov "US census data")) using zip code as the key. Please refer to the Entity Relationship Diagram for reference. 
![](database/ERD.png)

Please be noted that both loan data and census data have many columns, so for aesthetic purpose, only a few sample columns are shown in the diagram below. The metadata of census data can also be found in the respect folders in census data folder.

## Hypothesis statement

## Report

###  Week one 

#### Data cleaning and EDA
The intial data set consisted of 75 columns and 887379 rows. 
The initial step was to drop the columns with no values and check for relevant columns with null values.
the final clean data consisted of the 11 columns as shown in the fig below.

![img1](Resources/clean_data.jpg)

#### Data preprocessing
As suggested by the client, **"loan_status"** was made the label and the remaining columns was made into features.
Then all the features were encoded and teh follwing table was generated.

![img2](Resources/encoded_table.jpg)

### Exploratory data anaysis
Pearson corellation was used to see the correlation between the features to the label and the one with the highest corelation factor were decided to be made into features.

![img3](Resources/EDA.jpg)

Following columns were decided to be used for features : loan_amnt,	int_rate,	grades_value,	home_ownership,	annual_inc,	emp_length and label.

### Model descision
Two models were decided were decided and precision was made to be the priority to judge the model i.e. RANDOM FOREST and KNN MODEL were finalised.

## Random forest
Compare two new Machine Learning models that reduce bias to predict credit risk. The models classified 51,366 as High Risk and 246 as Low Risk.
![img4](Resources/random forest _count.jpg)

Balancedcount

BalancedRandomForestClassifier Model, two trees of the same size and equal size to the minority class are constructed to represent one for the majority class and one for the minority class.

The balanced accuracy score increased to 64.6 % for this model.

![img4](Resources/random_forest_accuracy.jpg)

The "Low Risk precision rate came to 0.95 with the recall at 0.64  giving this model an F1 score of  0.77. "High Risk" only had a precision rate of 15% with the recall at 65%. 

![img4](Resources/bal_clas_table.jpg)

![img4](Resources/bal_clas_classification.jpg)

## Ensemble classifier

EasyEnsembleClassifier Model, a set of classifiers where individual decisions are combined to classify new examples.

The balanced accuracy score increased to 64.6% with this model.

The "Low Risk precision rate increased to 95% with the recall at 64.6% giving this model an F1 score of 77.7%. "high Risk" still had a precision rate of 100% with the recall now at 65%.

![img5](Resources/ada_clas_classification.jpg)
![img5](Resources/ada_clas_table.jpg)

## Shortcoming of Week 1
low precision and low accuracy in both the models of random forest.

<img width="577" alt="random forest model img" src="https://user-images.githubusercontent.com/108248030/206589513-196512c7-328c-4208-a4a2-eda855f37dfe.png">


### Week two

KNN model was used to evaluate the model.
Initially it was assumed that the dataset was balanced and the KNN Model was used on the data set with the following results.

![img6](Resources/Mlenv_1_table.jpg)

![img7](Resources/Mlenv_1_classification.jpg)

Due to the dataset being imbalanced, random oversampling was used to balance the dataset.

![img8](Resources/mlenv_2_table.jpg)

![img9](Resources/mlenv_2_classification.jpg)

### Shortcomings in Week 2
Possiblity of overfitting of data needs to be evaluated.



### Week three 

number of loans and correlation with employment tenure

<img width="380" alt="image" src="https://user-images.githubusercontent.com/108248030/206610835-42472ef3-921a-49da-ac88-00593b99dd33.png">

As the table shows Employment tenure for more than 10 years had the highest number of applications


Loan status Total

<img width="472" alt="image" src="https://user-images.githubusercontent.com/108248030/206611192-565ce384-70c0-4d19-b227-1b2763b68571.png">


Home Ownership

<img width="477" alt="image" src="https://user-images.githubusercontent.com/108248030/206611247-55ccb236-782a-4d40-9b8e-9dbf18bde4fe.png">


Employee length vs Grade

<img width="616" alt="image" src="https://user-images.githubusercontent.com/108248030/206611324-3beddb74-de2a-4a43-96eb-d112faeaff3c.png">


Loan status vs employment length

<img width="407" alt="image" src="https://user-images.githubusercontent.com/108248030/206611395-b034c97f-4624-4236-9e0c-1f0591d3dda7.png">


Grade vs Home ownership

<img width="625" alt="image" src="https://user-images.githubusercontent.com/108248030/206611445-711f4563-c832-49ca-a566-3a4482d46636.png">


Tableau data: https://public.tableau.com/views/CreditDefaultAnalysisfromBankingInstitutions/Datacorelationandexploration?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

Google Slides presentation: https://docs.google.com/presentation/d/1RJUA9Z22VSU07C9NauIzTvf_5KOHWlUEm0I5xhRp-LE/edit?usp=sharing


