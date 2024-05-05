QuickStart Guide
================

Here, you will learn how to quickly launch the project on your local computer

Git
---
First, you need to go to this `repository <https://github.com/0R0bin/Python-OC-Lettings-FR/>`__

Then you need to **FORK** the project to your personnal Git. Make sure to **fork** the project! It's important for the in-depth configuration

Now that you have your project, simply clone it to your local computer from your link::

    https://github.com/<REPLACE_USER>/<PROJECT_NAME>
    

Venv
----
Now, let's create a virtual environment :

Unix/MacOS::

    python3 -m venv env

Windows::

    py -m venv env

And activate it

Unix/MacOS::

    source env/bin/activate

Windows::

    .\env\Scripts\activate

Then, install packages::

    pip install -r requirements.txt

SECRET_KEY
----------
Visit this `website <https://djecrety.ir/>`__ to generate your secret_key and keep it

SENTRY_SDK
----------
This project uses SentrySDK to log errors in the project

Follow these steps to get your link
    * Go to `sentry <https://sentry.io/welcome/>`__
    * Create an account
    * Create a project with the Django platform
    * Copy the dsn key

.env
----

Now that you have all the required informations, create a .env file here::

    oc_lettings_site/oc_lettings_site/.env

Your .env file should look like this::

    SECRET_KEY=secret_key_previous_step
    SENTRY_KEY_URL=sentry_key_previous_step

To be sure of the directory, .env should be placed in the same directory as settings.py

Last steps
----------
In your terminal go to oc_lettings_site *-the one containing all applications-*

And execute this command to collect static files::

    python manage.py collectstatic

Lastly, run the website::

    python manage.py runserver

You can now go to your localhost **http://127.0.0.0.1:8000**  and navigate through the website