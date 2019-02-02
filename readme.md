# PYTHON DATABASE REPORT # 

This is a class assignment for the Udacity Fullstack Web Developer nanodegree.

## Usage ##

To run the script, you need to have vagrant up and running with the setting files supplied on the class.

You will also need to set the views listed on the next topic.

Download the script to a convenient location. Once you moved to the script folder, run the command:

`python3 report.py`

It should create a report.txt file containing the output.


## Views ##

In order for the script to run properly, you need to set the following views on the database Udacity supplies:

> **View 1**
> 
> `create view author_view as select author, count(log) from articles, log where log.path like '/article/' || articles.slug group by author order by count desc;`
> 
> **View 2**
> 
>  `create view log_by_day as select date(time) as date, count(*) from log group by date;`
> 
> **View 3**
> 
> `create view errors_log as select date(time), count(*) from log where status = '404 NOT FOUND' group by date;`
> 
> **View 4**
> 
> `create view log_pct as select errors_log.date, (100.0 * errors_log.count/log_by_day.count) as pct from errors_log, log_by_day where errors_log.date = log_by_day.date;`

## Files ##

### report.py ###

This is the main script file. It is responsible for:

- Connecting to the database
- Creating the output file
- Executing the queries
- Writing the queries to output file with a helper function

### writer.py ###

Contains the report_writer helper function that formats the text before it is written to the output file.

It takes the string _title_ and the list _content_ as arguments. 

The argument _content_ is assumed to be a list of tuples,  each tuple containing two elements that correspond to columns of the sql table.
