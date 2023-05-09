banco-central-ts
================

Get data from the `Time Series Management System of the Central Bank of Brazil <https://www3.bcb.gov.br/sgspub/>`_, using its API.

The Central Bank of Brazil provides an API for collecting data from its Time Series Management System.
This library builds the necessary URL for the request and then uses a **pandas** function to request the data in CSV format and return a consistent time series.

Usage
-----

In this example, we collect data on the time series of code **12**, that is the time series **'Interest rate - CDI - %p.d. - daily**.
This time series is the daily `interbank deposits rate <https://pt.wikipedia.org/wiki/Certificado_de_Dep%C3%B3sito_Interbanc%C3%A1rio>`_.

.. code-block:: python

   import datetime as dt

   from banco_central_ts import get as bacen_ts

In order to collect the values of the time series for all available dates, the function is called without any arguments besides the series' code.

>>> cdi = bacen_ts(12)
>>> type(cdi)
pandas.core.frame.DataFrame
>>> cdi
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

In order to collect the values for a specific period, the **start** and **end** parameters must be used.

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

In order to collect the *n* most recent values of the time series, the **last_n** parameter must be used.
Note that this parameter overwrites the **start** and **end** parameters.

>>> bacen_ts(12, last_n=5)
               valor
data
2023-04-28  0.050788
2023-05-02  0.050788
2023-05-03  0.050788
2023-05-04  0.050788
2023-05-05  0.050788
