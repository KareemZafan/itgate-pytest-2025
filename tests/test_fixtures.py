import pytest

"""
@pytest.fixture
def open_db():
    print("\nOpenning DB\n")
    print("DB opened successfully")

@pytest.fixture
def close_db():
    yield
    print("\nClosing DB\n")
    print("DB closed successfully")
"""

@pytest.fixture(autouse=True,scope='module')
def open_close_db():
    print("\nOpenning DB\n")
    print("DB opened successfully\n")
    yield
    print("\nClosing DB\n")
    print("DB closed successfully\n")



def test_delete_from_db(): 
    print("\nDeleting from DB\n")
    print("row was deleted from DB")
    

def test_update_from_db(): 
    print("\nUpdating from DB\n")
    print("row was updated from DB")


def test_insert_into_db(): 
    print("\nInserting into DB\n")
    print("row was inserted from DB")

