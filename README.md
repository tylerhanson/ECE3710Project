# ECE3710Project

Colby Eyre, 10744831
Tyler Hanson, 10766582

### Description
This project uses an algorithm to rate college football teams. The algorithm is run against games in the past to collect the rating differential from the teams and the actual score differential. From this data, a linear regression line is then created to estimate for future games, given a rating differential, the expected score differential. This can be used to either predict outright winners or to find value in betting lines. 

### Setup
To execute the program, pull the code to a local repo, open a terminal at the root folder, and run
`python Main.py`
This will run the program against 50 games from 2019 and generate a plot for you to visualize. You can edit the range in line 14 of Main.py to run against more games however for time purposes I would recommend keeping it at 50.
