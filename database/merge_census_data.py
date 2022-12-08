import pandas as pd
import sqlalchemy as sql

engine=sql.create_engine('postgresql+psycopg2://Yuan:12345678@pgadmin.c4ari7frjjvy.us-east-2.rds.amazonaws.com:5432/final_project')

loan_data =pd.read_sql_table('loan_data', con=engine)
education =pd.read_sql_table('education', con=engine)
industry =pd.read_sql_table('industry', con=engine)
median_house_income =pd.read_sql_table('median_house_income', con=engine)

loan_data_enriched = \
loan_data.merge(education, how='left', left_on='zip_code', right_on='GEO_ID')\
         .merge(industry, how='left', left_on='zip_code', right_on='GEO_ID')\
         .merge(median_house_income, how='left', left_on='zip_code', right_on='GEO_ID')
         
loan_data_enriched

