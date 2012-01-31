SYNOPSIS
========

*pypstats* is for retrieving monthly download statistics for packages 
distributed via `PyPI <http://pypi.python.org/pypi>`_.  Statistics are 
downloaded from http://pypi.python.org/stats/months/.  This page contains 
monthly statistics in compressed files starting from June 2010.  These
files contains information on releases that are removed from PyPI, so
you will get more complete statistics for packages that were released 
after June 2010. 

INSTALLATION
============

Download **pypstats-1.{x}.tar.gz**. Extract tarball contents and run 
**setup.py** as follows::
  
  $ tar -xzf pypstats-1.x.tar.gz
  $ cd pypstats-1.x
  $ python setup.py install

Or, if if you have `Easy Install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_
installed, type the following::

  $ easy_install -U pypstats

USAGE
=====

First use
---------

Before statistics can be printed or plotted, you need to retrieve statistics 
and save them locally using **pypstats update** command::

  $ pypstats update ProDy
  Fetching content from 'http://pypi.python.org/stats/months/'.
  Parsing monthly statistics file details.
  Updating statistics for 2010-06.
  ...
  Updating statistics for 2012-01.
  Package statistics are updated (ProDy_stats.pkl).

Retrieving statistics at the first use will take some time, since all 
monthly stats files are downloaded.


Monthly stats
-------------

Monthly statistics can be printed using **pypstats monthly** command::

  $ pypstats monthly ProDy_stats.pkl 
  Loading statistics from 'ProDy_stats.pkl'.
  Month	Downloads
  2010-11	286
  ...
  2012-01	1041
  Total	  10664

This information can also be plotted and saved in a **.csv** file as 
follows::

  $ pypstats monthly -o monthly.csv -p monthly.png ProDy_stats.pkl
  Loading statistics from 'ProDy_stats.pkl'.
  Monthly statistics are written in 'monthly.csv'.
  Monthly downloads plot is saved as 'monthly.png'.
  
See an example plot here: http://www.csb.pitt.edu/ProDy/reports/pypi_statistics.html

Release stats
-------------

Release statistics can be printed using **pypstats release** command::


  $ pypstats release ProDy_stats.pkl 
  Loading statistics from 'ProDy_stats.pkl'.
  Release	Downloads
  0.1.0	397
  ...
  0.9.2	328
  Total	10664
  
Similarly, output can be written into a **.csv** file as follows::

  $ pypstats release -o release_stats.csv -q ProDy_stats.pkl
  
Note that **-q** argument suppresses messages written to **stderr**.

Total downloads
---------------

Total number of downloads can be printed using **pypstats total** command::

  $ pypstats total -q ProDy_stats.pkl 
  10664

Current release
---------------

Current release information can be retrieved using **pypstats current** 
command::

  $ pypstats current -q ProDy
  File	URL	md5	Type	Py Version	Size	Downloads
  ProDy-0.9.2.tar.gz	http://pypi.python.org/packages/source/P/ProDy/ProDy-0.9.2.tar.gz	9ad6f6e6012f824ea5e7acb344607eae	Source		711KB	119
  ProDy-0.9.2.win32-py2.6.exe	http://pypi.python.org/packages/2.6/P/ProDy/ProDy-0.9.2.win32-py2.6.exe	51f8587dcc8fe6d0355327d811ea71c3	MS Windows installer	2.6	455KB	47
  ProDy-0.9.2.win32-py2.7.exe	http://pypi.python.org/packages/2.7/P/ProDy/ProDy-0.9.2.win32-py2.7.exe	68ba279f3d9e02b38e4f3e6339b41b26	MS Windows installer	2.7	909KB	53
  ProDy-0.9.2.zip	http://pypi.python.org/packages/source/P/ProDy/ProDy-0.9.2.zip	b447f8b607defd5cda65163e43b32150	Source		744KB	109

This information can be written into a CSV file using reStructured Text style::

  $ pypstats current -q -o current_release.csv --rst ProDy
 
This file can be used in a page prepared using `Sphinx <http://sphinx.pocoo.org/>`_, 
see for an example: http://www.csb.pitt.edu/ProDy/getprody.html


Updates
-------

Local statistics file can be updated using **pypstats update** command::

  $ pypstats update ProDy
  Fetching content from 'http://pypi.python.org/stats/months/'.
  Parsing monthly statistics file details.
  Nothing to update.

This command will make an incremental update by downloading the files that
changed since the last update.

LICENSE
=======
  
*pypstats* is available under GNU General Public License version 3.  See 
LICENSE.txt for more details. 


SOURCE
======

http://github.com/abakan/pypstats


REPORT ISSUES
=============

https://github.com/abakan/pypstats/issues
  