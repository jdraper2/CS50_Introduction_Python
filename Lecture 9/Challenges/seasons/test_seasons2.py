import pytest
from seasons import calculate_date
from seasons import Seasons
from datetime import date

def main():
    today = date.today()
    today_str = (str(today)).split("-")
    

    today_minus_oneyear = str(date((int(today_str[0]))-1, int(today_str[1]), int(today_str[2])))
    today_minus_twoyear = str(date((int(today_str[0]))-2, int(today_str[1]), int(today_str[2])))

    me_one = Seasons(today_minus_oneyear)
    me_two = Seasons(today_minus_twoyear)

    test_default(today, me_one, me_two)

def test_default(t, one, two):
    assert calculate_date(one, t) == "five hundred and twenty-five thousand, six hundred minutes"
    assert calculate_date(two, today) == "one million, fifty-one thousand, two hundred minutes"

main()