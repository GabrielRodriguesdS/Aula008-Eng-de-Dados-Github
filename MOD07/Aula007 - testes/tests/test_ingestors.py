from asyncore import read
import datetime
from re import A
from unittest import mock
from unittest.mock import mock_open, patch
#from requests import patch
from ingestors import DataIngestor
from writers import DataWriter
import pytest

@pytest.fixture
@patch("ingestors.DataIngestor.__abstractmethods__", set())
def data_ingestor_fixture():
    return DataIngestor(
            writer = DataWriter,
            coins=["TEST", "HOW"],
            default_start_date=datetime.date(2022, 7, 1)
        )


@patch("ingestors.DataIngestor.__abstractmethods__", set())#criar patch é sobrescrever um método de uma classe
class TestIngestors:
    def test_checkpoint_filename(self, data_ingestor_fixture):
        actual = data_ingestor_fixture._checkpoint_filename
        expected = "DataIngestor.checkpoint"
        assert actual == expected

    def test_load_checkpoint_no_checkpoint(self ,data_ingestor_fixture):
        actual = data_ingestor_fixture._load_checkpoint()
        expected = datetime.date(2022, 7, 1)
        assert actual == expected

    @patch("builtins.open", new_callable=mock_open, read_data="2022-07-20")
    def test_load_checkpoint_existent_checkpoint(self, mock, data_ingestor_fixture):
        actual = data_ingestor_fixture._load_checkpoint()
        expected = datetime.date(2022, 7, 20)
        assert actual == expected

    @patch("ingestors.DataIngestor._write_checkpoint", return_value=None)
    def test__update_checkpoint_checkpoint_updated(self, mock, data_ingestor_fixture):
        data_ingestor_fixture._update_checkpoint(value=datetime.date(2022, 7, 5))
        actual = data_ingestor_fixture._checkpoint
        expected = datetime.date(2022, 7, 5)
        assert actual == expected

    @patch("ingestors.DataIngestor._write_checkpoint", return_value=None)
    def test__update_checkpoint_checkpoint_written(self, mock,data_ingestor_fixture):
        data_ingestor_fixture._update_checkpoint(value=datetime.date(2022, 7, 5))
        mock.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data="2022-07-20")
    @patch("ingestors.DataIngestor._checkpoint_filename", return_value="foobar.checkpoint")
    def test_write_checkpoint(self, mock_checkpoint_filename, mock_open_file, data_ingestor_fixture):
        data_ingestor_fixture._write_checkpoint()
        mock_open_file.assert_called_with(mock_checkpoint_filename, 'w')

