# django-starter

This is a starter kit for building a one page agency/app site. Use it to start your project and generate interest. Pivot and improve after that. It's also a great place to start to see how a basic Django project works.


Getting Started
------------------------
To setup your local environment you should create a virtualenv and install the
necessary requirements::

    mkvirtualenv starter
    pip install -r requirements.txt
    pip install -r requirements_dev.txt

Create a local settings file and set your ``DJANGO_SETTINGS_MODULE`` to use it::

    echo "export DJANGO_SETTINGS_MODULE=starter.settings.local" >> $VIRTUAL_ENV/bin/postactivate
    echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

Exit the virtualenv and reactivate it to activate the settings just changed::

    deactivate
    workon starter

You should now be able to run the development server::

    python manage.py runserver

I've already created an admin user for the local db with the username "admin" and the password "admin" with the email "admin@admin.com"

Requirements
------------------------
We've included Django Imagekit in the project so that we can do some image processing for background images and make that all work together.

