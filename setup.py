try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'name': 'NAME',
        'description': 'My Project',
        'author': 'Mark Paris',
        'url': 'https://github.com/mwparis/pythonProjectTemplate.git',
        'download_url': 'https://github.com/mwparis/pythonProjectTemplate.git',
        'author_email': 'mparis@lanl.gov',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
}

setup(**config)
