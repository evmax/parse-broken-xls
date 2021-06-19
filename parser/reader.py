import pandas as pd

from typing import List


# min size to exclude from table
DATA_FRAME_MIN_SIZE = 2


def read(file_path: str) -> List[pd.DataFrame]:
    """Reads xls file."""

    result = []

    # file corrupted, possibly was saved from email,
    # so read as html
    frames = pd.read_html(file_path, skiprows=12)

    for frame in frames:
        if frame.size > DATA_FRAME_MIN_SIZE:
            result.append(frame)

    return result
