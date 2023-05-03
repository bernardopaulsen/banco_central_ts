import datetime as dt
from unittest import TestCase
from unittest.mock import Mock, patch

from banco_central_ts import get as get_bcb_ts


class CsvExamplesTests(TestCase):
    """Examples from
    
    https://dadosabertos.bcb.gov.br/dataset/20542-saldo-da-carteira-de-credito-com-recursos-livres---total/resource/42454ae1-fea4-47df-b38a-101d8a62dbed?inner_span=True
    
    """
    def setUp(self) -> None:
        self.read_csv_mock = Mock()

    def _test_get_ts(self, url: str, **get_kwargs):
        with patch('pandas.read_csv', self.read_csv_mock):
            get_bcb_ts(
                code=get_kwargs['code'],
                start=get_kwargs.get('start'),
                end=get_kwargs.get('end'),
                last_n=get_kwargs.get('last_n')
            )
        self.read_csv_mock.assert_called_once_with(
            url,
            sep=';', decimal=',',
            index_col=0, parse_dates=True, dayfirst=True
        )

    def test_1(self):
        self._test_get_ts(
            url='https://api.bcb.gov.br/dados/serie/bcdata.sgs.20542/dados?formato=csv&dataInicial=01/01/2010&dataFinal=31/12/2016',
            code=20542,
            start=dt.datetime(2010, 1, 1),
            end=dt.datetime(2016, 12, 31)
        )

    def test_2(self):
        self._test_get_ts(
            url='https://api.bcb.gov.br/dados/serie/bcdata.sgs.20542/dados?formato=csv',
            code=20542
        )

    def test_3(self):
        self._test_get_ts(
            url='https://api.bcb.gov.br/dados/serie/bcdata.sgs.20542/dados/ultimos/10?formato=csv',
            code=20542,
            last_n=10
        )
