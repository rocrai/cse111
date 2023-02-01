from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Sally', 'Brown') == "Brown; Sally"
    assert make_full_name('Sa', 'Br') == "Br; Sa"
    assert make_full_name('Sally-Jane', 'Brown') == "Brown; Sally-Jane"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == 'Brown'
    assert extract_family_name("Br; Sa") == 'Br'
    assert extract_family_name("Sally-Jane; Brown") == 'Sally-Jane'
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == 'Sally'
    assert extract_given_name("Br; Sa") == 'Sa'
    assert extract_given_name("Brown-Jane; Sally") == 'Sally'
    assert extract_given_name("; ") == ""
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])