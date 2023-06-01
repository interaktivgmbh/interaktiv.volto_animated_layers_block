import sys

from pkg_resources import Requirement, parse_version
from setuptools import find_packages, setup

# Package metadata
NAME = 'interaktiv.volto_animated_layers_block'
DESCRIPTION = 'interaktiv volto_animated_layers_block product.'
URL = 'https://code.interaktiv.de/interaktiv/volto/interaktiv.volto_animated_layers_block'
EMAIL = 'support@interaktiv.de'
AUTHOR = 'Interaktiv GmbH'
REQUIRES_PYTHON = '~=3.10'
VERSION = '1.0.1'
REQUIRES_PLONE_VERSION = '6.0.0'

REQUIRED = [
    'setuptools',
    'Products.CMFPlone>=' + REQUIRES_PLONE_VERSION
]
EXTRAS = {
    'test': ['plone.app.testing']
}


# Check required python version
def check_python_version():
    required_python = Requirement.parse('python' + REQUIRES_PYTHON)
    current_version = parse_version(".".join(map(str, sys.version_info[:3])))
    if current_version not in required_python:
        sys.exit(f"'{NAME}' requires Python {REQUIRES_PYTHON} but the current Python is {current_version}")


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Do :: not :: publish"
    ],
    keywords='',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license='proprietary',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['interaktiv', ],
    include_package_data=True,
    zip_safe=False,
    python_requires=check_python_version(),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
)
