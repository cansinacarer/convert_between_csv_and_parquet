import sys
import pandas as pd

# Get the passed csv filename argument
csv_file = sys.argv[1]

# Read the csv and convert to parquet with the same name
df = pd.read_csv(csv_file)
df.to_parquet(f"{csv_file[:-4]}.parquet")
