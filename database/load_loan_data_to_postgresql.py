import pandas as pd
from sqlalchemy import create_engine

loan_data = pd.read_csv('./loan_data/loan.csv')
industry = pd.read_csv('./census_data/industry_occupation/ACSST5Y2020.S2405-Data.csv')
median_income = pd.read_csv('./census_data\median_household_income\ACSST5Y2020.S1901-Data.csv')
education = pd.read_csv('./census_data\education_attainment\ACSST5Y2020.S1501-Data.csv')

engine = create_engine("postgresql+psycopg2://Yuan:12345678@pgadmin.c4ari7frjjvy.us-east-2.rds.amazonaws.com:5432/final_project")

loan_data.to_sql('loan_data', con=engine, if_exists='append', index=False, chunksize=1000)
industry.to_sql('industry', con=engine, if_exists='append', index=False, chunksize=1000)
median_income.to_sql('median_household_income', con=engine, if_exists='append', index=False, chunksize=1000)
education.to_sql('education', con=engine, if_exists='append', index=False, chunksize=1000)