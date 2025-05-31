from src import calculator
import pytest

list_of_test_data = [(5,20,25),(-5,20,15),(-5,20,15),(5,-20,-15),(0,-20,-20)]
@pytest.mark.parametrize("input1,input2,expected_result",list_of_test_data)
def test_addition_functionality(input1, input2, expected_result):
   assert calculator.add(input1,input2) == expected_result


def test_subtraction_functionality():
   assert calculator.sub(5,20) == -15
   assert calculator.sub(-5,-20) == 15   
   assert calculator.sub(-5,20) == -25
   assert calculator.sub(5,-20) == 25
   assert calculator.sub(0,-20) == 20
   assert calculator.sub(5,0) == 5


@pytest.mark.FEB_RELEASE
@pytest.mark.Integeration
def test_multiplication_functionality():
   assert calculator.mul(5,20) == 100
   assert calculator.mul(-5,-20) == 100   
   assert calculator.mul(-5,20) == -100
   assert calculator.mul(5,-20) == -100
   assert calculator.mul(0,-20) == 0
   assert calculator.mul(5,0) == 0

@pytest.mark.Integeration
def test_division_functionality():
   assert calculator.div(20,20) == 1
   assert calculator.div(-5,-20) == 0.25   
   assert calculator.div(-5,20) == - 0.25
   assert calculator.div(20,-5) == -4
   assert calculator.div(0,-20) == 0
   assert calculator.div(5,0) == None


def test_absolute_functionality():
   assert calculator.abs(5) == 5
   assert calculator.abs(-5) == 5
   assert calculator.abs(0) == 0

def test_square_root_functionality():
   assert calculator.get_square_root(100) == 10
   assert calculator.get_square_root(625) == 25
   assert calculator.get_square_root(0) == 0
   
   

