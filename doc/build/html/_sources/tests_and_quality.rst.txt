Tests and Quality
=================

This section contains informations about unit tests and quality code

Quality
-------
To ensure that the code always remains maintainable, we use **Flake8**

In order to check code from your local computer, activate virtual environment
Then launch::

    flake8 .\oc_lettings_site\

If it returns nothing like below

.. figure:: assets/return_flake8.png
   :alt: Empty Return Flake8

Then the code doesn't contains any errors and your good to go

.. note::
    Configuration can be find in **setup.cfg**

Unit Tests
----------

In order to keep production in a stable version by writing unit test, pytest and coverage were implemented 

You can find these in every ../<app_name>/tests folder

For example
    * oc_lettings_site/lettings/tests/
    * oc_lettings_site/oc_lettings_site/tests/
    * oc_lettings_site/profiles/tests/

To launch them, activate virtual environment

Then launch::

    coverage run -m pytest ./oc_lettings_site

You should have this

.. figure:: assets/first_return_coverage.png
   :alt: First Return Coverage

From there you can launch::

    coverage report

And you can see coverage % here

.. figure:: assets/final_coverage.png
   :alt: Final Return Coverage

.. note::
    Configuration can be find in **setup.cfg**