from src import string as st
import pytest

def test_title():
    assert st.title("ali ahmed mahmoud") == "Ali Ahmed Mahmoud"

@pytest.mark.FEB_RELEASE
def test_capitalize():
    assert st.capitalize("ali ahmed mahmoud") == "Ali ahmed mahmoud"


def test_end_with():
    assert st.end_with("ali ahmed mahmoud","test") == False
    assert st.end_with("ali ahmed mahmoud","oud") == True

@pytest.mark.FEB_RELEASE
def test_split():
    assert st.split("ali ahmed mahmoud") == ["ali","ahmed","mahmoud"]
    assert st.split("many thanks dears") == ["many","thanks","dears"]
    
@pytest.mark.FEB_RELEASE
def test_toupper():
    assert st.toupper("ali ahmed mahmoud") == "ALI AHMED MAHMOUD"

def test_tolower():
    assert st.tolower("ALI AHMED MAHMOUD") == "ali ahmed mahmoud"  
    
    

