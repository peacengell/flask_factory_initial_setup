# flask_factory_initial_setup

### This repos will host all the minimum things needed when starting a new flask app.
flask_factory_initial_setup for starting new flask project

How to clone it:
#### git clone git@github.com:peacengell/flask_factory_initial_setup.git  [ NewFlaskApp ] Give it any name you want.

Then if you like you can create an virtual [ env ] like this : [ I would prefer you do this and not to mess-up wit your global python installation ]
    virtualenv env # the newly clone folder. To use specify python version in the env [ virtualenv env -p python3 ]
    Then source the env like this
    source env/bin/activate on linux/OSX
    source env/bin/activate.sh on windows
    Then pip install requirements.txt [ install all the requirement for Flask to work ]

Hola, now you are ready to code, and install any library you need using pip.
    Don't forget to do a pip freeze >requirements.txt, before sharing your code with anyone.

            settings.py  holds the secret_key and other settings needed.
            manage.py holds the command runserver to start the server with some variables, like
            activate debug
            reload on file changes
            host = 0.0.0.0
            port = 5000
            app.py is the main file for the app, all routes can go in this file.
            .gitignore file holds the files that you don't wana share.

    Do not hesitate to contact me if you need some help.
    I be glad to help you with. don't worry I am still new.
    Regards,

    peacengell@gmail.com

