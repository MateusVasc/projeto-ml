import pandas as pd
from typing import List

class Preprocessing:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def cols_to_numeric(self, columns: List[str]) -> pd.DataFrame:
        self.df[columns] = self.df[columns].apply(pd.to_numeric, errors='coerce')
        return self.df