You are in the tarpit, this may take longer than usual.
See https://www.pythonanywhere.com/tarpit for more information.
remote: Total 216 (delta 12), reused 213 (delta 12), pack-reused 0
Receiving objects: 100% (216/216), 1.31 MiB | 986.00 KiB/s, done.
Resolving deltas: 100% (12/12), done.
Updating files: 100% (229/229), done.
(trav) 08:23 ~ $ ls
README.txt  env  trav  travel1
(trav) 08:25 ~ $ cd travel1
(trav) 08:25 ~/travel1 (main)$ ls
README.md  travelproject
(trav) 08:25 ~/travel1 (main)$ cd travelproject
(trav) 08:25 ~/travel1/travelproject (main)$ ls
credentials  db.sqlite3  manage.py  static  templates  travelapp  travelproject
(trav) 08:26 ~/travel1/travelproject (main)$ pwd
/home/subhavinu32gmailcom/travel1/travelproject
(trav) 08:26 ~/travel1/travelproject (main)$ pip install django
(trav) 08:46 ~/travel1/travelproject (main)$ pip install pillow
trav) 09:01 ~/travel1/travelproject (main)$ pyhon manage.py makemigrations
bash: pyhon: command not found
(trav) 09:01 ~/travel1/travelproject (main)$ pyhon manage.py migrate
bash: pyhon: command not found
(trav) 09:01 ~/travel1/travelproject (main)$ python manage.py migrate
(trav) 09:02 ~/travel1/travelproject (main)$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
Error: That port is already in use.
(trav) 09:02 ~/travel1/travelproject (main)$ python manage.py runserver 8009