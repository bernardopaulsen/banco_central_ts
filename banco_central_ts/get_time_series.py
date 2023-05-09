import datetime as dt

import pandas as pd


__all__ = ['get']

BASE_URL = 'https://api.bcb.gov.br/dados'
FORMAT_URL = '?formato=csv'

CSV_OPTIONS = dict(sep=';', decimal=',')
INDEX_OPTIONS = dict(index_col=0, parse_dates=True, dayfirst=True)


def parse_datetime(
        datetime: dt.datetime
        ) -> str:
    return datetime.strftime('%d/%m/%Y')


def indexes_url(
        start: dt.datetime | None = None,
        end: dt.datetime | None = None
        ) -> str:
    return (
            ('' if start is None else f'&dataInicial={parse_datetime(start)}')
            + ('' if end is None else f'&dataFinal={parse_datetime(end)}')
    )


def last_url(
        last: int
        ) -> str:
    return f'/ultimos/{last}'


def series_url(
        code: int
        ) -> str:
    return f'/serie/bcdata.sgs.{code}/dados'


def build_url(
        code: int,
        start: dt.datetime,
        end: dt.datetime,
        last_n: int | None
        ) -> str:
    if last_n is not None:
        return BASE_URL + series_url(code) + last_url(last_n) + FORMAT_URL
    return BASE_URL + series_url(code) + FORMAT_URL + indexes_url(start, end)


def get(
        code: int,
        start: dt.datetime | None = None,
        end: dt.datetime | None = None,
        last_n: int | None = None
        ) -> pd.DataFrame:
    """Get time series data from Brazilian Central Bank.
    
    If `last_n` is given, the parameters `start` and `end` are ignored.

    :param code: Code of time series.
    :param start: First date.
    :param end: Last date.
    :param last_n: The number of observations to collect, starting from the most
        recent.

    :return: Time series.
    """
    return pd.read_csv(
        build_url(code, start, end, last_n),
        **CSV_OPTIONS, **INDEX_OPTIONS
    )
