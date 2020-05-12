## Comment Rating System
## Demo Website[website link](https://comment-rating-system.herokuapp.com/)

**templates/web.html**: The front end of this demo  
**Procfile**: Let Heroku, when starting the Web, execute gunicorn run: app -log-file-. The following -log-file-parameter is to make the log only print to the standard output stdout, because Heroku does not provide us the function to write to the local disk.  
**app.json**: Some introductions about this website  
**requirements.txt**: Some libraries and their versions required for the demo to run on Heroku.  
**run.py**: flask back end code  

## Install the Heroku CLI  
**Download and install the Heroku CLI.**  
**If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.**  
$ heroku login


## Clone the repository  
**Use Git to clone comment-rating-system's source code to your local machine.**  
$ heroku git:clone -a comment-rating-system
$ cd comment-rating-system  


## Deploy your changes
**Make some changes to the code you just cloned and deploy them to Heroku using Git.**  
$ git add .  
$ git commit -am "make it better"  
$ git push heroku master  
