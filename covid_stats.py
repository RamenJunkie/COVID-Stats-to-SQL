# Python Covid Star Tracking to SQL
# use of json package
# Sample URL: https://covidtracking.com/api/states?state=IL

import json
import requests
import time
import MySQLdb

mydb = MySQLdb.connect(
  host="localhost",
  user="YOUR_DB_USERNAME",
  passwd="YOUR_DB_PASSWORD",
  database="YOUR_DB_NAME"
)
mycursor = mydb.cursor()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

#States to check as an Array, two letter abbreviations
states = ['IL']

def data_getter(statename):
  ####when reading from remote URL
  url = 'https://covidtracking.com/api/states?state='+statename

  user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
  headers = {'User-Agent': user_agent}
  response = requests.get(url,headers=headers)
  html = response.content
  statedata = json.loads(html)

  pos_cases = (statedata['positive'])
  neg_cases = (statedata['negative'])
  deaths = (statedata['death'])

  vals = (pos_cases,neg_cases,deaths,statename)

  mysqlinsert(vals)

def mysqlinsert(vals):
  ## This database name and columns can be changed but should be pre made in your database
  SQL = "INSERT INTO covid_stats (positive_cases, negative_cases, deaths, state) VALUES (%s, %s, %s, %s)"
  mycursor.execute(SQL, vals)
  mydb.commit()

# Loop through URLs for each state
for i in states:
  data_getter(i)