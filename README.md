## Preparation
Import `yummy.sql` into your MySQL database. Then, change the 
username and password in backend/src/yummyModel.py to your local
settings.

Install python 3 environment. Then use pip to install `flask` 
and `peewee` packages.

Install node environment (my version: 11.15.0).

## Run
First use python 3 to start the back end in backend/src/:
```
$ python backend/src/app.py
```

Then use npm to start the front end in frontend/:
```
$ cd frontend
$ npm install && npm run dev
```
