def test_zero_dev():
    with pytest.raises(Exception):
        n_days(0)

