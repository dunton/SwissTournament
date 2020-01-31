# Swiss Tournament

This is a database of a swiss style tournament allowing you to add players, report matches and clear previous results.

### Set-Up

You must install vagrant in order to run  this program. After vagrant is 
installed you can unzip **Dunton_Tournament**. The zipped file should
contain:

* **Vagrantfile**
* **pg_config.sh**
* **README**
* A folder named **Tournament** containing:
    * **tournament**.**py**
    * **tournament.pyc**
    * **tournament_test.py**
    * **tournament.sql**

### Tournament File Information
* **tournament**.**py**
    * Defines functions to run through the PSQL database to enable functionality
* **tournament.pyc**
    * Compiled version of tournament.py
* **tournament_test.py**
    * Tests suite to verify the code in tournament.py
* **tournament.sql**
    * Contains the database and table information for Dunton_Tournament
### Running the Program

First "vagrant up" to launch the vm then sign in using "vagrant ssh".

It is crucial to navigate to the proper 'vagrant' directory. Once set up with vagrant navigate out past 'home' so you see a listing of 22 directories such as 'bin', 'boot', 'dev', 'etc', and 'home' among others. Go to the 'vagrant' directory then into 'tournament'. 

We need to setup the database. After navigating into the 'tournament' directory type `psql`. Then type `CREATE DATABASE tournament;` to create the database. After creating the database type `\q` . Once back in the 'vagrant' interface type 
`psql tournament < tournament.sql` to import the database specifications. 

Finally type `python tournament_test.py` to test the program.
