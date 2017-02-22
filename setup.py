from setuptools import setup
from setuptools import find_packages

required_packages = [
    'beautifulsoup4',
    'cssselect',
    'duckling',
    'feedfinder2',
    'feedparser',
    'idna',
    'jieba3k',
    'JPype1',
    'Logbook',
    'lxml',
    'newspaper3k',
    'nltk',
    'Pillow',
    'PyQt5',
    'python-dateutil',
    'PyYAML',
    'requests',
    'requests-file',
    'sip',
    'six',
    'tldextract',
    'wit', ]


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='alfred',
      version='0.1',
      description='Modular Bot',
      url='https://github.com/Sefrwahed/Alfred',
      author='Sefrwahed',
      author_email='Sefrwahed@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=required_packages,
      entry_points={
          'console_scripts': [
              'alfred = alfred.__main__:main']},
      zip_safe=False, )
