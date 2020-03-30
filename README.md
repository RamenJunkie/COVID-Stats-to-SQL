# COVID-Stats-to-SQL

A Python Script to import COVID-19 stats from a web API and dump them into an SQL database.

You will need to set up the database in SQL before running the script.  A schema file is included but you can also manually create the database. Nothing complicated, mostly INT fields. an id as an int and primary key, negative_cases, positive_cases, and deaths, all as INT, state as a varchar with a length of 2, though technically the length is optional, then finally date_stamp as a DATETIME field with a default value of the current timestamp. The DATETIME isn’t directly touched here, but it makes it easier to manipulate the data later.

The code also requires you enter your database credentials and rename the database table to match the table you have set up. I’ve nammed my table “covid_stats, but you can change that to whatever you want in the “SQL = “INSERT….” line. I’ll leave it up to you what to do with the data, I pull mine into a PHP page.

You will also need to set the state or states you want to check in the states array.

You can run this script manually or using a schedule such as cron (I run my daily).  It will dump time stamped stats into the table for each state in the array.  The data can then be pulled and displayed using whatever method you want (I display mine on a local website using PHP).
