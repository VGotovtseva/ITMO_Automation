def test_hw():
    assert ('home', 'work') == ('home', 'work')


def test_qaqc():
    assert 'QA' != 'QC'


def test_number():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)


