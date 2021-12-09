Thoth's TensorFlow stack guidance example
-----------------------------------------

**See different branches for different examples**

This is an example of an application which uses Thoth's recommendations to
recommend a TensorFlow stack for a specific hardware. The application is
showing one of the `Integration of Thoth
<https://pypi.org/project/thamos>`_ using Thamos CLI.

For OpenShift s2i (Source-To-Image) examples, visit `thoth-station/s2i-example
<https://github.com/thoth-station/s2i-example>`__ repository.

Thamos CLI
==========

One of the integration for Thoth is `Thamos
<https://pypi.org/project/thamos>`_. You can use Thoth's recommendation engine
directly from within your terminal. First, you need to clone this repo and
install Thamos CLI:

.. code-block:: console

  git clone https://github.com/thoth-station/cli-example.git && cd cli-example
  pip3 install thamos
  thamos --help

The pre-configured template for Thamos CLI is available in the
``.thoth.yaml`` file:

.. code-block:: console

  cat .thoth.yaml

Alternatively, to generate Thoth's configuration file out of the template run the
following command:

.. code-block:: console

  thamos config --no-interactive --template thoth_conf_template.yaml
  cat .thoth.yaml  # to browse the content of the config file

Now you are ready to ask for advises:

.. code-block:: console

  thamos advise

This might take some time. Once Thoth recommends you the application stack to
be used for running the application, create a Python environment and install
requirements into it:

.. code-block:: console

  pip3 install micropipenv

In order to obtain requirement.txt, you can use the following command:

.. code-block:: console

  micropipenv requirements --no-dev

Finally install the requirements in your environment:

.. code-block:: console

  cat requirements.txt  # check requirements with digests
  python3 -m venv venv/ && . venv/bin/activate
  micropipenv install

And finally, run the application (the virtual environment needs to be still
activated):

.. code-block:: console

  python3 ./app.py

To browse Thoth's logs during or after the adviser run:

.. code-block:: console

  thamos log

Manage vulnerablities in your dependencies with an example application 
----------------------------------------------------------------------

The ``game_of_life.py`` program is a simple application that shows how Thamos manages known vulnerablities in the dependencies of a project.
To use this example application, follow the steps mentioned above relative to the installation of the Thamos CLI and to its configuration using ``.thoth.yaml``.

To introduce voluntarily a known vulnerability in the project, specify that you would like to add ``numpy`` version 1.13.1 in your requirements:

.. code-block:: console

  thamos add numpy==1.13.1

This version of ``numpy`` is known for introducing a vulnerability further described on the `National Vulnerability Database website 
<https://nvd.nist.gov/vuln/detail/CVE-2017-12852>`_.
Thamos can also manage user requirements for dependencies using `constraints files
<https://pip.pypa.io/en/stable/user_guide/#constraints-files>`_. To add ``numpy`` version 1.13.1 in your dependency requirements this way, you can simply write the package with its version into this file.

To get a stack guidance based on security, run the following command:

.. code-block:: console

  thamos advise --recommendation-type security

or modify the ``recommendation_type`` field to ``security`` in ``.thoth.yaml`` to set it as your default recommendation type, and simply run:

.. code-block:: console

  thamos advise

Thamos report should show that ``numpy`` 1.13.1 was automatically removed from your application software stack as a CVE was found in the package.

Run the example application
===========================

Now that you know how Thamos prevents the use of unsafe direct dependencies in your application, you can revert to another version of ``numpy`` to complete this part of the tutorial.
To run the example application with the resolved dependencies, run:

.. code-block:: console

  python3 game_of_life.py

to launch a new game with the default parameters or choose your own parameters as specified in the ``help`` section.
Click on the coordinates to select your first generation of individuals and press ``Enter`` to see the next generation.