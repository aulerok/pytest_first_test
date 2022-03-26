
from app.calculate import Calculator

class TestCalc_Positive:
    def setup(self):
        self.calc = Calculator

        """ позитивный тест умножения для калькулятора """
    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

        """позитивный тест деления для калькулятора"""
    def test_division_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

        """позитивный тесты вычитания для калькулятора"""
    def test_substaction_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

        """позитивный тесты сложения для калькулятора"""
    def test_adding_correclty(self):
        assert self.calc.adding(self, 2, 2) == 4

class TestCalc_Negative:
    def setup(self):
        self.calc = Calculator

        """ негативный тест умножения для калькулятора """
    def test_multiply_incorrectly(self):
        assert self.calc.multiply(self, 2, 2) != 4

        """негативный тест деления для калькулятора"""
    def test_division_incorrectly(self):
        assert self.calc.division(self, 2, 2) != 1.0

        """негативный тест вычитания для калькулятора"""
    def test_substraction_incorrectly(self):
        assert self.calc.subtraction(self, 2, 2) != 0

        """негативный тест сложения для калькулятора"""
    def test_adding_incorrectly(self):
        assert self.calc.adding(self, 2, 2) != 4
