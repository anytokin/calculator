from powerful_calculator import Calculator
import itertools

calc = Calculator()

def test_calculator():
    calc = Calculator()
    assert calc.add(5.0)==5.0
    assert calc.add(10.0)==15.0
    assert calc.subtract(10.0)==0.0
    assert calc.multiply(5)==0.0
    assert calc.add(0.1)==0.1
    assert calc.add(0.2)==0.3
    assert calc.get_state()==0.3
    assert calc.reset()==0
    assert calc.subtract(-15.00)==15.0
    assert calc.divide(3.0)==5.0
    assert calc.multiply(-3.0)==-15.0
