''' setup '''
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

#here = os.path.abspath(os.path.dirname(__file__))
with open('README.md') as f:
    readme = f.read()


config = {
    'name': 'tpsautomation',
    'version': '0.1',
    'description': 'TPS automation project',
    'author': 'Jack',
    'author_email': 'bin.meng@ourunited.com',
    'url': 'https://github.com/mengbinhao/tpsautomation',
    'download_url': 'https://github.com/mengbinhao/tpsautomation',
    'tests_require': ['pytest', 'pytest-html', 'pytest-rerunfailures'],
    'packages': ['tpsautomation'],
    #packages=find_packages(exclude=('tests', 'docs')),
    'scripts': [],
    'install_requires': ['pywinauto', 'pyautogui', 'autopep8', 'pylint', 'rope', 'virtualenv', 'mkvirtualenv'],
    'license': ''
    # 'setup_requires': ['pytest-runner'],
    # 'entry_points': {
    #     'console_scripts': [
    #         'tpsautomation = tpsautomation.cli:main'
    #     ]
    # },
    # 'classifiers': (
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # )
}
setup(**config)
