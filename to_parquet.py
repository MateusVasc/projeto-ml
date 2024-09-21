import pandas as pd
from typing import List
from pathlib import Path

def to_parquet(dir_path: str, df_list: List[str]) -> None:
    for s in df_list:
        path = Path(dir_path) / s
        
        if not path.is_file():
            print(f'File {path} does not exist')
            continue
        
        path_parquet = path.with_suffix('.parquet')

        df = pd.read_csv(path)
        df.to_parquet(path_parquet)
        path.unlink()
        print(f"Arquivo {s} convertido para Parquet e excluído.")


dir_path: str = 'data'
df_list: List[str] = ['air_quality.csv', 'diabetes_dataset.csv', 'out.csv']
to_parquet(dir_path, df_list)