# PYTHON DATABASE REPORT # 

This is a class assignment for the Udacity Fullstack Web Developer nanodegree.

## Usage ##

To run the script, you first need to have _python 3_ installed. You can [get python here](https://www.python.org/downloads/). Choose the correct version for your system and follow the installer instructions.

You will also need to get _virtual box_ using [this link](https://www.virtualbox.org/wiki/Downloads) and _vagrant_ using [this one](https://www.vagrantup.com/downloads.html). Be sure to pick the correct version for your system and follow the installation instructions.

Once you have both installed, download the virtual machine configuration files (which contains the database that will be used by the script) using [this link](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) or by cloning [this repository](https://github.com/udacity/fullstack-nanodegree-vm).

Unzip the configuration files on a convenient directory and move to them using a shell, then move to the directory vagrant and execute the command `vagrant up`. After it is done, execute `vagrant ssh`.

If everything goes right, you will have to move to the _/vagrant_ directory inside your virtual machine. This directory is shared with your computer. The script of this repository must be downloaded and stored on the /vagrant directory.

You will also need to set the views listed on the next topic.

Once everything is done, move to the directory you store this script (remember it must be inside the /vagrant directory) and run the command:

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
