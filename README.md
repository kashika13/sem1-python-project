# sem1-python-project
This is a project on Cyber Cafe Management System. It is in very preliminary state and not connected with any database. I have made this project using csv files.
<br>
It contains 4 files:
1. Python code file: It contains code of the project.
2. ccms: It contains details of the user.
3. priority_user: It contains the list of priority users.
4. A word file: It contains the code and the screenshot of the output.



Instructions to run the code:

This code uses datetime module, random module and prettytable module. Before executing the code make sure that all these modules are installed in the python IDLE.
or This code can also be executed online on Replit.


About the project:

It contains one main driver code and 6 user-defined functions.
1. register: It takes details from user and write it into ccms file.
2. login: It uses random module to create userID.
3. read: It reads the ccms file.
4. cabin: It allots cabin to user after taking their userId as input. Total number of cabins avialable is 7.
5. bill: It uses random module to generate the usage hour of a user and then calculate the bill. Hourly price is 100 Rs.
6. p_user: It finds the priority user based on cabin allocation and store them in priority_user file.

