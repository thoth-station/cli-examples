Manage vulnerablities in your dependencies with an example application
----------------------------------------------------------------------

**See different branches for different examples**

This is an example of an application which uses Thoth's recommendations to
recommend a software stack for specific security requirements. The application is
showing one of the `Integration of Thoth
<https://pypi.org/project/thamos>`_ using Thamos CLI.

For OpenShift s2i (Source-To-Image) examples, visit `thoth-station/s2i-example
<https://github.com/thoth-station/s2i-example>`__ repository.

Running the application
=======================

One of the integration for Thoth is `Thamos
<https://pypi.org/project/thamos>`_. You can use Thoth's recommendation engine
directly from within your terminal. First, you need to clone this example repo
and install Thamos CLI:

.. code-block:: console

  git clone https://github.com/thoth-station/cli-example.git && cd cli-example
  pip3 install thamos
  thamos --help

The pre-configured template for Thamos CLI is available in the
``.thoth.yaml`` file:

.. code-block:: console

  cat .thoth.yaml

Now you are ready to ask for advises:

.. code-block:: console

  thamos advise

This might take some time. Once Thoth recommends you the application stack to
be used for running the application, you can use Thamos to create a Python
environment (based on configuration in ``.thoth.yaml``) and install the
recommended requirements into it:

.. code-block:: console

  thamos install

And finally, run the application:

.. code-block:: console

  thamos run ./game_of_life.py

To browse Thoth's logs produced during the resolution:

.. code-block:: console

  thamos log

About the application
=====================

The ``game_of_life.py`` program is a simple application that shows how Thamos
manages known vulnerablities in the dependencies of a project.  To use this
example application, follow the steps mentioned above relative to the
installation of the Thamos CLI and to its configuration using ``.thoth.yaml``.

To introduce voluntarily a known vulnerability in the project, specify that you would like to add ``pillow`` version 8.0.0 in your requirements:

.. code-block:: console

  thamos add pillow==8.0.0

This version of ``pillow`` is known for introducing a vulnerability further described on the `pypa/advisory-db repository
<https://github.com/pypa/advisory-db/blob/main/vulns/pillow/PYSEC-2021-94.yaml>`_.
Thamos can also manage user requirements for dependencies using `constraints files
<https://pip.pypa.io/en/stable/user_guide/#constraints-files>`_. To add ``pillow`` version 8.0.0 in your dependency requirements this way, you can simply write the package with its version into this file.

To get a stack guidance based on security, run the following command:

.. code-block:: console

  thamos advise --recommendation-type security

or modify the ``recommendation_type`` field to ``security`` in ``.thoth.yaml`` to set it as your default recommendation type, and simply run:

.. code-block:: console

  thamos advise

Thamos report should show that an error occured during the resolution process because a known vulnerability was found in``pillow`` version 8.0.0 .

Run the example application
===========================

Now that you know how Thamos prevents the use of unsafe dependencies in your application, you can revert to another version of ``pillow`` to complete this part of the tutorial.
To run the example application with the resolved dependencies, run:

.. code-block:: console

  thamos run ./game_of_life.py

To launch a new game with the default parameters or choose your own parameters as specified in the ``help`` section.
Click on the coordinates to select your first generation of individuals and press ``p`` to see next generations.
