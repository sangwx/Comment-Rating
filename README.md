## Comment Rating System
## Demo Website[website link](https://comment-rating-system.herokuapp.com/)

**templates/web.html**: The front end of this demo
**Procfile**: Let Heroku, when starting the Web, execute gunicorn run: app -log-file-. The following -log-file-parameter is to make the log only print to the standard output stdout, because Heroku does not provide us the function to write to the local disk.
**app.json**: Some introductions about this website
**requirements.txt**: Some libraries and their versions required for the demo to run on Heroku.
**run.py**: flask back end code

Deploy the demo on Heroku:

```
mkdir /home/heroku/comment-rating     # Create local code working directory
cd /home/heroku/comment-rating        # Switch to the local code working directory
git init                                    # Create a local code base
heroku git:remote -a comment-rating   # Connect to the remote Heroku flask-bjhee code base
```
Push local git repository to Heroku remote repository:
```
git add .
git commit -m "New update"
git push heroku master 
```
See website deployment effect:
```
heroku open
```
