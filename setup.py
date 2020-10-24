import pathlib
from setuptools import setup
import sys
if sys.version_info[0] < 3:
    raise Exception("Sorry, you must use Python 3")

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf-8')

setup(
    name='ponisha_projects',
    description="""This is a Scrapy project to scrape projects from [ponisha.ir](https://ponisha.ir).""",
    url='https://github.com/rferdosi/ponisha_projects',
    maintainer='rferdosi',
    version='1',
    packages=['ponisha_projects', 'ponisha_projects.spiders'],
    install_requires=['scrapy', 'selenium',
                      'scrapy-selenium', 'pymongo[srv]', 'schedule'],
    classifiers=["Programming Language :: Python :: 3", ],
    license='The MIT License',
    long_description=README,
    long_description_content_type="text/markdown"
)
