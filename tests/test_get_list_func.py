from utils.get_success_operations import success_operations


def test_func():
    assert success_operations('./tests/test1.json') == []
    assert success_operations('./tests/test2.json') == []
    assert success_operations('./tests/test3.json') == []
