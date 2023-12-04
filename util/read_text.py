from pathlib import Path
from typing import List

def get_all_lines(path: Path) -> List[str]:
    with open(path) as f:
        return [line for line in f.readlines() if len(line) > 0]

def get_input_file_path(day: int) -> Path:
    current_file_dir = Path(__file__).parent.absolute()
    input_file_path = current_file_dir.parent.joinpath("puzzles").joinpath(f"day{day}").joinpath("input.txt")
    assert input_file_path.is_file()
    return input_file_path

def get_input_lines(day: int) -> List[str]:
    return get_all_lines(get_input_file_path(day))
