# Surfs Up

In this project, I created a weather API based on weather measurements and weather station data in Hawaii that were provided in CSV files. I used the Jupyter Notebook for most of my work on this API. The first step was the data engineering step. In this step, I inspected the data inside the CSV files to see if it needed to be cleaned. I did this by reading the CSV files with pandas. When I inspected the data frame I created I saw that the data from the CSV file containing the weather measurements had a considerable amount of “NaN” values in the precipitation column. I chose to leave the “NaN” values in because I didn’t want to make assumptions about the data. 

The next step in the process was database engineering. In this step, I created the SQLite database for my weather API. I used pandas and SQLAlchemy and the CSV files that I was provided to create my SQLite database.

The third step in creating my weather API was to do a climate analysis based on the data that was stored in the SQLite database that I created. In this step, I analyzed the data using SQLAlchemy to do queries on the data. I then used Pandas to create data frames so I could create graphs using Matplotlib.

The final step was to create a Flask app to power my weather API. I exported my climate analysis Jupyter Notebook as a Python file. I then added the required Flask routes so the app would run.

