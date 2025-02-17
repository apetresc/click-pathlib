"""
Setup script.
"""

from pathlib import Path
from typing import List

import versioneer
from setuptools import find_packages, setup


def _get_dependencies(requirements_file: Path) -> List[str]:
    """
    Return requirements from a requirements file.

    This expects a requirements file with no ``--find-links`` lines.
    """
    lines = requirements_file.read_text().strip().split('\n')
    return [line for line in lines if not line.startswith('#')]


_DIRECT_REQUIRES = _get_dependencies(
    requirements_file=Path('requirements.txt'),
)

_INDIRECT_REQUIRES = _get_dependencies(
    requirements_file=Path('indirect-requirements.txt'),
)

INSTALL_REQUIRES = _DIRECT_REQUIRES + _INDIRECT_REQUIRES

DEV_REQUIRES = _get_dependencies(
    requirements_file=Path('dev-requirements.txt'),
)
PACKAGING_REQUIRES = _get_dependencies(
    requirements_file=Path('packaging-requirements.txt'),
)

LONG_DESCRIPTION = Path('README.rst').read_text()

setup(
    name='click-pathlib',
    version=versioneer.get_version(),  # type: ignore
    cmdclass=versioneer.get_cmdclass(),  # type: ignore
    author='Adam Dangoor',
    author_email='adamdangoor@gmail.com',
    description=(
        'A Python click type which is similar to click.Path but returns a '
        'Pathlib path'
    ),
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where='src'),
    zip_safe=False,
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    keywords='click',
    include_package_data=True,
    license='MIT',
    url='https://github.com/adamtheturtle/click-pathlib',
    extras_require={
        'dev': DEV_REQUIRES,
    },
    classifiers=[
        'Operating System :: POSIX',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
    ],
    # Avoid dependency links because they are not supported by Read The Docs.
    #
    # Also, they require users to use ``--process-dependency-links``.
    dependency_links=[],
)
