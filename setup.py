import platform
from distutils.core import setup

if platform.system() == 'Windows':
    SCRIPTS = ['pypstats.py']
else:
    import shutil
    shutil.copyfile('pypstats.py', 'pypstats')
    SCRIPTS = ['pypstats']

with open('README.rst') as inp:
    long_description = inp.read()

setup(
    name='pypstats',
    version='1.0',
    author='Ahmet Bakan',
    author_email='ahmetbakan at msn dot com',
    description='Retrieve monthly package download statistics from PyPI',
    long_description=long_description,
    url='https://github.com/abakan/pypstats',
    py_modules=['pypstats'],
    license='GPLv3',
    keywords=('monthly, package, download, statistics'),
    scripts=SCRIPTS,
    classifiers=[
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Operating System :: MacOS',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                ],
    )
