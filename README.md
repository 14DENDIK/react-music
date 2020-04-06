# react-music
React Django Music App
## Installation
After creating virtual environment run following:
```bash
pip3 install -r requirements.txt
```
Then inside frontend folder:
```bash
npm install
```
Database is Postgresql, you should create it in your PC.
If don't like the headache of setting new database, just stick with SQLite but don't forget to edit settings!
## About
Just made this app for learning "djangorestframework", "reactjs", and authenticating users through tokens, for this I used simplejwt.
Both front and backend run on the same server which makes usage of CORS uneccassary.(But makes the app slower)
Works pretty fast and good, BUT had some problems with client side routing of ReactJS.
Didn't want to spend too much time for learning front side...
## About Django side
Used:
  *Django rest framework
  *Postgresql
  *Django rest framework simple jwt(for token auth)
## About React side
Didn't use npx create-react-app
Used:
  *React Routing
  *Hooks
  *Context API(Don't know maybe removed)
## Screen
![Screen](https://github.com/14DENDIK/react-music/blob/master/media/re.png)
