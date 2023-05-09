.. banco-centrql-ts documentation master file, created by
   sphinx-quickstart on Wed May  3 14:58:20 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to banco-central-ts's documentation!
===========================================

Get data from the Time Series Management System of Brazilian Central Bank

Usage
-----

.. code-block:: python

   import datetime as dt

   from banco_central_ts import get as bacen_ts

>>> bacen_ts(12)
               valor
data
1986-03-06  0.068111
1986-03-10  0.069028
1986-03-12  0.067417
1986-03-14  0.064584
1986-03-17  0.068222
              ...
2023-04-28  0.050788
2023-05-02  0.050788
2023-05-03  0.050788
2023-05-04  0.050788
2023-05-05  0.050788

>>> bacen_ts(12, start=dt.datetime(2022, 4, 28), end=dt.datetime(2022, 5, 6))
               valor
data
2022-04-28  0.043739
2022-04-29  0.043739
2022-05-02  0.043739
2022-05-03  0.043739
2022-05-04  0.043739
2022-05-05  0.047279
2022-05-06  0.047279

>>> bacen_ts(12, last_n=5)
               valor
data
2023-04-28  0.050788
2023-05-02  0.050788
2023-05-03  0.050788
2023-05-04  0.050788
2023-05-05  0.050788

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   modules/api
   modules/license



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
