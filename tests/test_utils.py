import pytest

from main import convert_date, masking_card


def test_convert_date():
    assert convert_date("2018-06-30T02:08:58.425572") == "30.06.2018"
    assert convert_date("2018-03-23T10:45:06.972075") == "23.03.2018"

def test_masking_card():
    assert masking_card("MasterCard 7158300734726758") == 'MasterCard 715830**6758'
    assert masking_card("Счет 35383033474447895560") == 'Счет **5560'
