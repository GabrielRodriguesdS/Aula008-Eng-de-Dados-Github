import datetime

from apis import DaySummaryApi

class TestDaySummaryApi:
    def test_get_data(self):
        actual = DaySummaryApi(coin="BTC").get_data(date=datetime.date(2022, 7, 1))
        expected = {'date': '2022-07-01', 'opening': 106665.4551465, 'closing': 102274.10620692, 'lowest': 100153.86164575, 'highest': 106744, 'volume': '6635444.58196999', 'quantity': '64.33945431', 'amount': 
5120, 'avg_price': 103131.8131795}
        assert actual == expected

    def test_get_data_better(self):
        actual = DaySummaryApi(coin="BTC").get_data(date=datetime.date(2022, 7, 1)).get("date")
        expected = "2022-07-01"
        assert actual == expected
