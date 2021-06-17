import os
from typing import List

import datetime
import pandas as pd


def _write_as_csv(out_dir: str, index: int, frame: pd.DataFrame) -> str:
    """Write to csv."""
    # add datetime to make files not
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = os.path.join(out_dir, f"{now}_{index}.csv")
    frame.to_csv(filename, index=False)
    return filename


def write(out_dir: str, filename: str, data: List[pd.DataFrame]) -> List[str]:
    """Writes content into files and return paths to files."""
    paths = []
    for idx, frame in enumerate(data, 1):
        paths.append(_write_as_csv(out_dir, idx, frame))
    return paths
