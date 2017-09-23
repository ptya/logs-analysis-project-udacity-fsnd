# Logs Analysis Udacity Project :star:
This is my Logs Analysis project for Udacity's Full Stack Developer Nanodegree.

It is a Python script using psycopg2 to run queries on a mock PostgreSQL database
for a fictional news website.

It generates a console output for three reports:
1. Top 3 articles, most viewed first.
2. Most popular authors, most viewed first.
3. Days above 1% request errors


### Mock database structure
#### Table "authors"

|Column|Type|
|---|---|
|name| text|
|bio| text|
|id|integer|

Primary key:
- id

#### Table "articles"

|Column|Type|
|---|---|
|author| integer|
|title| text|
|slug| text|
|lead| text|
|body| text|
|time| timestamp with time zone |
|id| integer|

Primary key:
- id

Foreign-key:
- author REFERENCES authors(id)


#### Table "log"

|Column |Type|
|---|---|
|path| text|
|ip| inet|
|method| text|
|status| text|
|time| timestamp with time zone |
|id| integer|

Primary key:
- id

# Installation :coffee:
### Prerequisites: :video_game:
- [Installed VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Installed Vagrant](https://www.vagrantup.com/downloads.html)
- [Downloaded VM from Udacity](https://github.com/udacity/fullstack-nanodegree-vm)
- [Downloaded DB for `news` database (`newsdata.sql`)](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


### Environment setup :boom:
1. Unzup and copy the `newsdata.sql` file from `newsdata.zip` to your vagrant directory
1. Start the VM using your console in the downloaded Vagrant VM's directory using `vagrant up`
1. SSH into your VM using `vagrant ssh`
1. To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`


### Application setup :wave:
1. Create a new directory in vagrant's shared directory (i.e.: `../vagrant/logs_analysis/`)
1. Clone the repository and put it into the previously created directory. (i.e.: `../vagrant/logs_analysis/`)


# Usage :computer:
1. SSH into your VM using `vagrant ssh`
2. `cd` into the created folder (i.e.: `/vagrant/logs_analysis`)
3. Run `./reporting.py`

An example of the output can be seen in `output_example.txt`

# License :trollface:
Copyright (c) 2017 Péter Szabó. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
