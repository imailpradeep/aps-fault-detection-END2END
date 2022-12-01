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
26. In Terminal 'git reset --soft 6afd' enter then 'git log' enter to verify then 'git add .' then 'git status'
27. git commit -m "This is the first version of code"
28. We get error message since it oes not have our details like email address
29. git config --global user.email "you@example.com" and git config --global user.name "Your Name", now commit
30. git push origin main -f to push our files to git hub 
31. -f was used to 'forcefully' only once as the history was not related but next time onwards no need to use -f
32. "git add ." enter and 'git commit -m "Added a new file .gitignore"'enter to add new file "git push origin main"
33. .gitignore has a lsit of file names not uploaded or tracked byt github
34. git -status gives list of files in read which are not synced. so 'git add filename' then 'git commit -m "message"'
35. lastly 'git push origin main' but if we get error then 'git pull origin main' and if there are conflicts the file will come up in red on left side
36. click on any red files and accept or reject changes and "git add ." and 'git commit -m "message" and git push again 

37. Make 'sensor' folder and create 'setup.py' file inside it. setup file is necessary for portability 
38. the find_packages() knows which packages have python in it by looking for __init__.py file 
39. in the setup file we give information like author name, etc.
40. in requirements folder insert all the required packages list 
41. in the setup file now we need to write a function for a list of strings containing the packages list
42. in requirements.txt every line ends with \n (new line character) and it needs to be removed
43. also since we need to install our source code as library we need '-e .' in the requirements.txt
44. -e means editable and . means current folder (such as terminal$ cd ./sensor aand in terminal$ git add .)
45. but -e . gives error hence we need to remove it from the list to run the rest of the list. -e . triggers setup.py file when running requirements.txt
46. when we complete the setup.py file and run it then after that pip install -r requirements.txt does not give error
47. the __init__.py causes sensor folder to be shown in sensor.egg-info/sources.txt but not 'notebook' folder as it does not have it
48. inside sensor create component folder to store the components of the pipeline line data cleaning, validation, etc.
49. entity folder is created to store the different outputs of the different predictions and artifacts
50. __init__.py is to be created it we want to convert the folder to package, helper functions may be required so make utils folder for them
51. entity folder has config_entity.py for defining inputs and artifact_entity.py for defining outputs


52. 'Data Ingestion', 'Data Validation', 'Data Transformation', 'Model Trainer', 'Model Evaluation', 'Model Pusher'.
53. all the above need config and artifact (input and output), so creatgite class for them in config_entity.py and artifact_entity.py
54. the ... is same as 'pass' 
55. inside components folder also we need the six files 
56. in pipeline folder we add training_pipeline.py to contain files
57. all programs need logger.py and exception.py
58. after writing code for logging and exception we can import necessary output to main


