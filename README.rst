Approaches to logging data operations performed with Pandas
===========================================================

An investigation into logging data operations performed using the `Pandas <https://pandas.pydata.org/>`_ data analysis Python library.

.. image:: https://travis-ci.com/sedelmeyer/pandas-logging.svg?branch=master
    :target: https://travis-ci.com/sedelmeyer/pandas-logging

.. image:: https://github.com/sedelmeyer/pandas-logging/workflows/build/badge.svg?branch=master
    :target: https://github.com/sedelmeyer/pandas-logging/actions

.. contents:: Contents
  :local:
  :depth: 1
  :backlinks: none

Summary
-------

This project is an investigation into potential approaches for logging data operations conducted using the Python ``pandas`` library.

I often find the need to document and review data pipelines used to cleanse data or engineer features used in my analyses. However:

  * Short of reviewing the actual code used to perform those data operations, actions performed uing ``pandas`` leaves no record;

  * Because ``pandas`` does not natively implement any logging functionality, changes made to data operations are not always readily available for later review unless care was taken to manually document changes to those operations.

A log-stream saved to file would provide an auditable and portable record of actions performed on the data under analysis. It would also have the potential to provide a human-readable record that could be reviewed by non-developer analysts seeking to replicate the analysis using some sort of GUI analytics software such as Excel or Tableau.

Therefore, this project is an investigation into potential approaches to achieve this sort of logging functionality in a repeatable manner.

.. note::

    * This project is starting from a point of personal exploration, and the degree to which I codify my findings into something useful for others to use still has yet to be determined.

    * Therefore, documentation related to this investigation will likely be sparse unless/until I happen upon meaningful findings or an approach of real use.

Potential existing solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a starting point, this project contains the source code for two separate Open Source Python libraries written by authors other than myself:

1. ``pdlog``, written by `Wasim Lorgat <https://github.com/seeM>`_, and hosted by the `DataProphet <https://github.com/DataProphet>`_ GitHub organization: https://github.com/DataProphet/pdlog

2. ``pandas-log``, written by `Eyal Trabelsi <https://github.com/eyaltrabelsi>`_ and located at: https://github.com/eyaltrabelsi/pandas-log

My initial intent is to:

a. Explore, in-depth, the methods employed by these two libraries,
b. Learn from the efforts of these two library authors,
c. Consider their methods relative to approaches I have attempted in previous projects of my own.

.. note::

    **All sections below are still just boilerplate. Thus, they do not reflect any specifics having to do with this project.**

Analysis and findings
---------------------

The analysis and findings associated with this project can be found here:

https://sedelmeyer.github.io/pandas-logging

Source code documentation
-------------------------

Documentation for the python modules built specifically for this analysis (i.e. modules located in the ``./src/`` directory of this project) can be found here:

https://sedelmeyer.github.io/pandas-logging/modules.html

.. _replication:

Replicating this analysis
-------------------------

In order to replicate this analysis and run the Python code available in this analysis locally, follow these steps:

.. contents:: In this section
  :local:
  :backlinks: none

.. todo::

    * Below is a placeholder template containing typical steps required to replicate a PyData project.
    * Content must be added to each section, outlining requirements and explaining how to replicate the analysis locally

0. Ensure system requirements are met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Clone this repository locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2. Install the required environment using Pipenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3. Run the data pipeline and analysis workflows locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4. Explore the associated Jupyter notebooks included with this project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _development:

Adding to this project
----------------------

If you'd like to build off of this project to explore additional methods or to practice your own data science and development skills, below are some important notes regarding the configuration of this project.

.. contents:: In this section
  :local:
  :backlinks: none

.. todo::

    * Below are placeholder sections for explaining important characteristics of this project's configuration.
    * This section should contain all details required for someone else to easily begin adding additional development and analyses to this project.

Project repository directory structure, design, and usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python package configuration and associated workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Testing
^^^^^^^

Version control and git workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Documentation using Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _issues:

Questions or issues related to this project
-------------------------------------------

.. todo::

    * Add details on the best method for others to reach you regarding questions they might have or issues they identify related to this project.


.. _sources:

Sources and additional resources
--------------------------------

.. todo::

    * Add links to further reading and/or important resources related to this project.
