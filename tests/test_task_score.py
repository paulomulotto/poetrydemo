import pytest
from taskscordepm.task_score import calculate_task_score


class TestCalculateTaskScore:
    def test_edge_cases(self):
        """
        Test with minimum and maximum importance and effort values.
        """
        assert calculate_task_score(1, 1) == 25
        assert calculate_task_score(4, 4) == 25

    def test_min_value(self):
        """
        Test with minimum importance and maximum effort values.
        """
        assert calculate_task_score(1, 4) == 6

    def test_max_value(self):
        """
        Test with maximum importance and minimum effort values.
        """
        assert calculate_task_score(4, 1) == 100

    def test_happy_path(self):
        """
        Test with moderate importance and effort values, and equal importance and effort values.
        """
        assert calculate_task_score(2, 3) == 17
        assert calculate_task_score(3, 3) == 25

    def test_exceptions(self):
        """
        Test with importance and effort values below and above the minimum and maximum values.
        """
        with pytest.raises(ValueError):
            calculate_task_score(0, 2)

        with pytest.raises(ValueError):
            calculate_task_score(5, 2)

        with pytest.raises(ValueError):
            calculate_task_score(3, 0)

        with pytest.raises(ValueError):
            calculate_task_score(3, 5)
