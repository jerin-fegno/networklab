# HackBOX Basic CTF Challenges 
#### Built over Django Framework
Hackbox is a networklab which contains 10 small web development challenges covering basic level web fundamentals and 
JavaScript.

## General Guidelines and Hints
*    Always check the source code of the page to find how it is working or if there are any hints that can help you understand the flow.
*    Think about how the page might be working normally. General clues can help with this. If you find it hard to follow, just remember that general programs always execute line by line.
*    You can inspect a webpage to edit an HTML page and run whatever you want to get it displayed there. If there is a hidden field, consider how you might change its value.
*    Browsers handle cookies and user agents. Try to understand what they mean.
*    File extensions are just virtual indicators. They help to guess the application with which it should be work best with.
*    There are different number systems, such as decimal, binary, and ASCII, and we can apply operations like arithmetic, conditional, or even logical operations on them. There are many online tools for this.
*    There are different encoding systems such as ASCII, URL encode, and HTML encoding that can help to save the web from misinterpreting content.
*    Hidden files like robots.txt or sitemap.xml can help search engines find other files or directories. A 404 error can sometimes help as well.


It is important to identify and report any bugs in the system. These challenges were created quickly for your entertainment!

## Challenges
* [Challenge - 1994](http://localhost:8000/challenge-1994/)
* [Challenge - Break Login Fault](http://localhost:8000/challenge-break-login-fault/)
* [Challenge - Crash IT](http://localhost:8000/challenge-crash-it/)
* [Challenge - Encoder Specialist](http://localhost:8000/challenge-encoder-specialist/)
* [Challenge - Explorer](http://localhost:8000/challenge-explorer/)
* [Challenge - Fake The Role](http://localhost:8000/challenge-fake-the-role/)
* [Challenge - Master Manipulator](http://localhost:8000/challenge-master-manipulator/)
* [Challenge - Torture](http://localhost:8000/challenge-torture/)
* [Challenge - Tough Analyzer](http://localhost:8000/challenge-tough-analyzer/)
* [Challenge - What Happened](http://localhost:8000/challenge-what-happened/)


## Manual Deployment
It is recommended to Ubuntu OS based instances for development and Deployment. Though, any contribution should take care of cross platform capability of te application. 
To deploy the Django application for production, follow these steps:


1. Clone the repository into your directory. (Preferred: `/var/www/networklab/`)
2. Create a virtualenv named `venv` in the project directory.
```commandline
virtualenv -p /usr/bin/python3.8 venv
 ```
3. each time you enter into project Activate the virtual environment:
```commandline
source venv/bin/activate
```

4. Install Requirements from `requirements.txt`:
 ```commandline
 pip install -r requirements.txt
 ```
5. Run migrations:
 ```commandline
python manage.py migrate
```
6. Collect static files:
 ```commandline
python manage.py collectstatic --noinput

```
7. Test the application by running the development server:
 ```commandline
 python manage.py runserver 0.0.0.0:8000
 ```
   If everything is working fine, proceed with the deployment on nginx using gunicorn and systemd.  

8. Install Gunicorn:
 ```commandline
 pip install gunicorn
 ```
9. Create a systemd service file for Gunicorn. For that save this file as `hackbox.service` in the directory `/etc/systemd/system/`.
You can use the command
```
sudo nano /etc/systemd/system/hackbox.service
```


10. Copy and paste the below code into the `hackbox.service` and press `[ctrl] + [o]` then `[enter]` to save the file and to quit press `[CTRL] + [X]`
``` commandline
[Unit]
Description=Gunicorn daemon for Hackbox

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/var/www/networklab/
ExecStart=/var/www/networklab/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/tmp/networklabchallenge.sock hackbox.wsgi:application

[Install]
WantedBy=multi-user.target
```

11. Create a systemd service file for Gunicorn. For that save this file as `hackbox.socket` in the directory `/etc/systemd/system/`.
You can use the command
```
sudo nano /etc/systemd/system/hackbox.socket
```

12. Copy and paste the below code into the `hackbox.socket` and press `[ctrl] + [o]` then `[enter]` to save the file and to quit press `[CTRL] + [X]`
``` commandline
# /etc/systemd/system/hackbox.socket

[Unit]
Description=Gunicorn socket for Hackbox

[Socket]
ListenStream=/tmp/networklabchallenge.sock

[Install]
WantedBy=sockets.target
```

13. Start the Gunicorn socket:
```commandline
sudo systemctl start hackbox.socket
```

14. Enable the Gunicorn socket to start at boot time:
```commandline
sudo systemctl enable hackbox.socket
```

15. Start the Gunicorn service:
```commandline
sudo systemctl start hackbox.service
```

16. Enable the Gunicorn service to start at boot time:

```commandline
sudo systemctl enable hackbox.service
```

17. Configure Nginx to serve the application:
```commandline
# /etc/nginx/sites-available/networklab.conf

server {
    listen 80;
    server_name networklab.yourdomain.com;

    location /assets/ {
        alias /var/www/networklab/public/assets/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/tmp/networklabchallenge.sock;
    }
}
```

18. Save this configuration file as `/etc/nginx/sites-available/networklab.conf` and create a symbolic link to it in the directory `/etc/nginx/sites-enabled/.`  with the command
```commandline
sudo ln -s /etc/nginx/sites-available/networklab.conf /etc/nginx/sites-enabled/networklab.conf
```

19. Test the Nginx configuration:
```
sudo nginx -t
```

20. Reload Nginx to apply the changes:

```
sudo systemctl reload nginx
```

That's it! Your Django application should now be up and running on your production server.

## Docker Deployment
Please note that this environment has not been tested. I Would like to bring up your Pull requests against documentations and issues. 
for now to setup the project in docker. User the command 

> docker-compose up --build

This will build the Docker image and start the container. The application should now be accessible at http://localhost:8000.

to change the port number, change the "0.0.0.0:8000" to your wish  ip:port in the last line of `Dockerfile`
```
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hackbox.wsgi:application"]
```

For Flag mode, you can use @fbctf, and for Simple Mode, you can use @CTFd.


# Customizing Challenge Flags

To customize the #challenge_flags alter values the values in `hackbox/settings.py. Remember  this is python file. take care of that if you are not comfortable with python.

```python3

ARENA = {
    "LOCATION": "Project Network Lab",  # Projecting Challenge name in page titles.
    "USER_AGENT": "Pehia",      # A solution to challenge #C009 depends on this word. 
    "ASSISTANT_EMAIL": "assistant@pehialabs.org",       # A solution to challenge #C001 uses this as default email. 
    "CHALLENGE_NAME": "Pehia CTF",      # Projecting Challenge name in meta descriptions
}

ARENA_FLAGS = {
    'C001': "LABS&PEHIA123",
    'C002': "CARDIAC1234",
    'C003': "BINCRACKER",
    'C004': "INDEXRANKING",
    'C005': "HTMLENTITIES",
    'C006': "PARIS",                # You have to upload curresponding Morse code to public/static/challenges/morse.wav
    'C007': "BUFFERZONE",
    'C008': "ARENACRACKER",
    'C009': "AGENTMODIFIER",
    'C010': "SESSIONEXPERT",
}


```
