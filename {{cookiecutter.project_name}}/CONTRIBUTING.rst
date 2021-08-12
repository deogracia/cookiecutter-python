Contributor Guide
=================

Thank you for your interest in improving this project.
This project is open-source under the `{{cookiecutter.license.replace("-", " ")}} license`_ and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- `Source Code`_
- `Documentation`_
- `Issue Tracker`_

.. _{{cookiecutter.license.replace("-", " ")}} license: https://spdx.org/licenses/{{cookiecutter.license}}.html
.. _Source Code: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
.. _Documentation: https://{{cookiecutter.project_name}}.readthedocs.io/
.. _Issue Tracker: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues

How to report a bug
-------------------

Report bugs on the `Issue Tracker`_.

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.


How to request a feature
------------------------

Request features on the `Issue Tracker`_.


How to set up your development environment
------------------------------------------

You need Python 3.6+ and the following tools:

- Pyenv_
- Poetry_

Install the needed python version by looking in the .python-version file

.. code:: console

  $ cat .python-version
  # 3.7.11
  # 3.8.11
  # 3.9.6
  # 3.6.14
  $ pyenv install 3.7.11
  $ pyenv install 3.8.11
  $ pyenv install 3.9.6
  $ pyenv install 3.6.14

Install the package with development requirements:

.. code:: console

   $ poetry install

You can now run an interactive Python session,
or the command-line interface:

.. code:: console

   $ poetry run python
   $ poetry run {{cookiecutter.project_name}}

.. _Pyenv: https://github.com/pyenv/pyenv
.. _Poetry: https://python-poetry.org/


How to test the project
-----------------------

Run the full test suite:

.. code:: console

   $ poetry run nox

List the available Nox sessions:

.. code:: console

   $ poetry run nox --list-sessions

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

.. code:: console

   $ poetry run nox --session=tests

Unit tests are located in the ``tests`` directory,
and are written using the pytest_ testing framework.

.. _pytest: https://pytest.readthedocs.io/


How to submit changes
---------------------

Open a `pull request`_ to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before commiting your change, you can install pre-commit as a Git hook by running the following command:

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

.. _pull request: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/pulls
