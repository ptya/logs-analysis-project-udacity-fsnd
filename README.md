# Logs Analysis Udacity Project :star:
This is my Logs Analysis project for Udacity's Full Stack Developer Nanodegree.

# Installation :coffee:
### Prerequisites: :video_game:
- Downloaded VM from Udacity
- Downloaded DB for `news` database (`newsdata.sql`)


### Environment setup :boom:
1. Copy the `newsdata.sql` file to your vagrant directory
1. Start the VM using your console in the downloaded Vagrant VM's directory using `vagrant up`
1. SSH into your VM using `vagrant ssh`
1. To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`


### Application setup :wave:
1. Clone the repository and put it into vagrant's catalog directory. (i.e.: `../vagrant/catalog/`)


# Usage :computer:
1. SSH into your VM using `vagrant ssh`
2. `cd` into `/vagrant/catalog`
3. Run `python reporting.py`

An example of the output can be seen in `output_example.txt`

# License :trollface:
Copyright (c) 2017 Péter Szabó. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
