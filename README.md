# J.P. Morgan Chase software engineering program 

## Starter repo and setting up dev environment
###
Fork and clone the starter repo here: https://github.com/theforage/forage-jpmc-swe-task-1
IMPORTANT! Uncheck the “Copy the main branch only” box in the fork dialog on GitHub. A model answer has been provided in a separate branch from main.

Create a new virtual environment in the project root. You can create a virtual environment using the venv module in Python:
$python -m venv venv  
This will create a new directory named venv in your project root, containing the virtual environment.

Activate the Virtual Environment (windows  /  linux):
$.\venv\Scripts\activate     /     $source venv/bin/activate

Install all project dependencies. These are listed in the requirements.txt file:
$pip install -r requirements.txt


## Interface with a stock price data feed.
You’ve been asked to assist with some development to add a chart to a trader’s dashboard allowing them to better identify under/over-valued stocks.

The trader would like to be able to monitor two historically correlated stocks and be able to visualise when the correlation between the two weakens (i.e. one stock moves proportionally more than the historical correlation would imply). This could indicate a potential trade strategy to simultaneously buy the relatively underperforming stock and sell the relatively outperforming stock. Assuming the two prices subsequently converge, the trade should be profitable.

Most data visualisation for our traders is built on JPMorgan Chase's Perspective data visualisation software, which is now open source. If you want to explore that, a link is provided in the resources section.

Before implementing this request using perspective, first, you’ll need to interface with the relevant financial data feed and make the necessary adjustments to facilitate the monitoring of potential trade opportunities.


## The tasks (already completed)
Fix the broken client datafeed script in the repository by making the required adjustments to it.
(optional) Add unit tests in the test script in the repository.


## To run 
###
First, type in the terminal:
$python server3.py

then, open a new terminal, and type:
$python client3.py