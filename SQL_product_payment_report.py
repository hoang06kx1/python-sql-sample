# imports for SQL data part
import pyodbc
from datetime import datetime, timedelta
import pandas as pd

# imports for sending email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

cnxn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQL2K2;DATABASE=SampleDB;Trusted_Connection=yes;'

date = datetime.today() - timedelta(days=7)  # get the date 7 days ago

date = date.strftime("%Y-%m-%d")  # convert to format yyyy-mm-dd

cnxn = pyodbc.connect(cnxn_str)  # initialise connection (cnxn_str should be defined before hand)

# build up our query string
query = ("SELECT * FROM customers "
         f"WHERE joinDate > '{date}'")

# execute the query and read to a dataframe in Python
data = pd.read_sql(query, cnxn)

del cnxn  # close the connection

# make a few calculations
mean_payment = data['payment'].mean()
std_payment = data['payment'].std()

# get max payment and product details
max_vals = data[['product', 'payment']].sort_values(by=['payment'], ascending=False).iloc[0]

# write an email message
txt = (f"Customer reporting for period {date} - {datetime.today().strftime('%Y-%m-%d')}.\n\n"
       f"Mean payment amounts received: {mean_payment}\n"
       f"Standard deviation of payment amounts: {std_payments}\n"
       f"Highest payment amount of {max_vals['payment']} "
       f"received from {max_vals['product']} product.")

# print out the result
print(txt)