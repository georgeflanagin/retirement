# retirement
A retirement calculator

There are many calculators. I have been increasing my familiarity 
with datetime and dateutil.

This calculator uses argparse to let you change its operation.

```
usage: retirement.py [-h] --birthday BIRTHDAY --hiredate HIREDATE
                     [--min-age MIN_AGE] [--req-years REQ_YEARS]
                     [--magic-number MAGIC_NUMBER]
```

`birthday` most formats are recognized.

`hiredate` same formats as birthdate.

`min-age` in years, but non-integers are not currently supported.

`req-years` also in whole years.

`magic-number` often, there is some value that is usually the sum of years of service and age.

Example:

```
python retirement.py --birthday "April 23 1975" --hiredate "Jan 2 2010" --min-age 60

Exit date: 2035-04-23 in 5798 days
Old enough: 2035-04-23
Long enough: 2020-01-02
You are now 16117 days old
You have been working here 3444 days
```
