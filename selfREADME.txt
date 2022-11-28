### Notes

MAKE MONGODB FILE
1. Made MongoDB + Python as the Neurolab file 
2. On the left side MongoDB tab we have nmake new connection and used the link given in 'main.py'
3. then used wget 'link to csv file' ( local folder of MongoDB) in Terminal
4. Now we will put the csv in MongoDB and then take data from there
5. Create a file named data_dump.py. In it copy paste the import pymongo and connection link from main.py
6. In data_dump.py create a database and collection but needs pandas for reading csv files 
7. hence write pandas in requirements.txt and in terminal we write - 'pip install -r requirements.txt'
8. right click csv data file in workspace and click 'copy path' paste it in the data_dump.py file 
9. after data_dump.py is complete run it by typing 'python data_dump.py' in Terminal
10. we need to convert the data from csv to .json and put in MongoDB
11. CODE TO CONVERT TO JSON IN DATA_DUMP.Py
12. click mongo tab on left side and in Connections refreshby collapsing and expanding tree
13. Now inserted data into mongoDB and next start project

MAKE GIT-HUB LINK
14. create new repo in github but in .gitignore choose pyth
15. connect github to CODE but check that main branch in github and main in the bottom left corner
16. in Terminal type 'git remote -v' and already iNeuron git is connected and the name is origin as per the Terminal output
17. type 'git remote remove origin' and remove old connection
18. type 'git log' to see versions 
19. create new git connection and name by convention is origin but we can give any name 
20. git remote add origin https://github.com/imailpradeep/aps-fault-detection-END2END.git
21. first we need to fetch the code to github and then push hence we get .gitignore in the workspace
22. Git tries to match the first instance but they do not match hence the error which needs to be removed
23. 'ls -a' gives a list of all files folders, git log files are saved in folders (cd and cat commands)
24. when we do a soft or hard reset we need to give the first 4 (or few) characters of the latest previous git log
25. the Head -> main has been moved to the git which you gave the characters

