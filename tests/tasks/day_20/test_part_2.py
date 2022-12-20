from aoc.common.storage import get_data_path
from aoc.tasks.day_20.part_2 import go

TEST_PATH = get_data_path(__file__, "test.txt")


def test_day_20_part_2_go():
    assert go(TEST_PATH) == 1623178306
