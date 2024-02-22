import pytest
import Factorial

def test_unit_calculate():
  # Arrange
  n = 4
  expected = 24
  # Act
  result = Factorial.calculate(n)
  # Assert
  assert result == expected

@pytest.mark.parametrize("n,expected",
  [ (1,1), (5,120), (7,5040), (9,362880) ])
def test_unit_calculate2(n,expected):
  assert Factorial.calculate(n) == expected
