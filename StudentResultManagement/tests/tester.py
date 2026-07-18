import pytest
from models import StudentManager

manager = StudentManager()

def test_grade_A():
    assert manager.get_grade_point(90) == 4.0

def test_grade_B():
    assert manager.get_grade_point(78) == 3.0

def test_grade_C():
    assert manager.get_grade_point(67) == 2.0
def test_grade_D():
    assert manager.get_grade_point(55) == 1.0
def test_grade_F():
    assert manager.get_grade_point(40) == 0.0