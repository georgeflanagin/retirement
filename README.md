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
