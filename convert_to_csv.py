import sys
import pandas as pd

# Get the passed csv filename argument
parquet_file = sys.argv[1]

# Read the csv and convert to parquet with the same name
df = pd.read_parquet(parquet_file)
df.to_csv(f"{parquet_file[:-4]}.csv")
