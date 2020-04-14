Thoth's TensorFlow stack guidance example
-----------------------------------------

**See different branches for different examples**

This is an example of an application which uses Thoth's recommendations to
recommend a TensorFlow stack for a specific hardware. The application is
showing one of the `Integration of Thoth
<https://pypi.org/project/thamos>`_ using Thamos CLI.

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
