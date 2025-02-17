Contributing
============

Release Process
---------------

Outcomes
~~~~~~~~

* A new ``git`` tag available to install.
* A new package on PyPI.

Prerequisites
~~~~~~~~~~~~~

* ``python3`` on your ``PATH`` set to Python 3.6+.
* ``virtualenv``.
* Push access to this repository.
* Trust that ``master`` is ready and high enough quality for release.

Perform a Release
~~~~~~~~~~~~~~~~~

#. Install keyring

   Make sure that `keyring <https://pypi.org/project/keyring/>`__ is available on your path.

   E.g.:

   .. code:: sh

      curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python
      pipsi install keyring

#. Set up PyPI credentials

Register at `PyPI <https://pypi.org>`__.

Add the following information to `~/.pypirc`.

.. code:: ini

   [distutils]
    index-servers=
        pypi

    [pypi]
    username = <Your PyPI username>

Store your PyPI password:

.. code:: sh

   keyring set https://upload.pypi.org/legacy/ <Your PyPI username>

#. Get a GitHub access token:

   Follow the `GitHub instructions <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`__ for getting an access token.

#. Set environment variables to GitHub credentials, e.g.:

    .. code:: sh

       export GITHUB_TOKEN=75c72ad718d9c346c13d30ce762f121647b502414
       export GITHUB_OWNER=adamtheturtle

#. Perform a release:

    .. code:: sh

       curl https://raw.githubusercontent.com/"$GITHUB_OWNER"/click-pathlib/master/admin/release.sh | bash
