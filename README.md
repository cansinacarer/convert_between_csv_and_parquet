This is the script that is called by ACC to convert a csv file to a parquet file.

Install its dependencies while ignoring other yum errors:

`yum install nano wget python3 --disablerepo=pgdg94 --disablerepo=pgdg95 --disablerepo=pgdg96`

Install program dependencies:

`python3 -m pip install pandas==1.1.5 Cython==0.29.33 pyarrow==0.13.0`

Then run the program with:

`python3 convert_to_parquet.py test.csv`

Put this py file in a folder that neolane owns.
