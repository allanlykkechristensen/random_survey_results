import generate
import datetime


class TestRandomDate:

    def test_one_entry(self):
        # Given
        start_date = datetime.datetime.strptime("20200110", "%Y%m%d")
        end_date = datetime.datetime.strptime("20200120", "%Y%m%d")
        entries = 1

        # When
        observed = generate.random_date(start_date, end_date, entries)

        # Then
        assert len(observed) == 1

    def test_ten_entries(self):
        # Given
        start_date = datetime.datetime.strptime("20200110", "%Y%m%d")
        end_date = datetime.datetime.strptime("20200120", "%Y%m%d")
        entries = 10

        # When
        observed = generate.random_date(start_date, end_date, entries)

        # Then
        assert len(observed) == 10
