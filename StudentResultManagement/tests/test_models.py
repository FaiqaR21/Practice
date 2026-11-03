
import pytest
from models import StudentManager


@pytest.fixture
def manager():
    obj = StudentManager()
    yield obj
    obj.close()


def test_grade_A(manager):
    assert manager.get_grade_point(90) == 4.0


def test_grade_B(manager):
    assert manager.get_grade_point(78) == 3.0


def test_grade_C(manager):
    assert manager.get_grade_point(67) == 2.0


def test_grade_D(manager):
    assert manager.get_grade_point(55) == 1.0


def test_grade_F(manager):
    assert manager.get_grade_point(40) == 0.0


def test_grade_boundary(manager):
    assert manager.get_grade_point(85) == 4.0
    assert manager.get_grade_point(75) == 3.0
    assert manager.get_grade_point(65) == 2.0
    assert manager.get_grade_point(50) == 1.0
