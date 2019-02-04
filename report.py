#!/usr/bin/env python3

import psycopg2
from writer import report_writer


# Prepare a text file to register the results
report = open('report.txt', 'w+')
report.write('Python Database Report \r\n\r\n')

# Set the database connection
try:
    db = psycopg2.connect(database='news')
except psycopg2.Error as e:
    print ("Unable to connect to the database")

c = db.cursor()

# Collection of queries to be executed
queries = [
    """select title, count(log) from articles,
    log where log.path like '/article/' ||
    articles.slug group by title order by count desc limit 3;""",
    """select authors.name, count from authors, author_view
    where authors.id = author_view.author;""",
    "select * from log_pct where pct > 1;"
]

results = []

# Executes all queries in a loop
for query in queries:

    c.execute(query)
    results.append(c.fetchall())

# Write the results to a text file, using the report_writer helper function.
report.write(report_writer('Most popular articles', results[0]))
report.write(report_writer('Most popular authors', results[1]))
report.write(report_writer('Too many requisition errors', results[2]))

db.close()
report.close()
