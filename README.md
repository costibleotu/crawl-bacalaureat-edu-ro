# crawl-bacalaureat-edu-ro

This is a crawler for [bacalaureat.edu.ro](www.bacalaureat.edu.ro). It lets you crawl any year (from 2004 to present),
and exports data in csv or json.

## Environemnt setup
```bash
mkvirtualenv --python=python3 <virtualenv_name>
pip install -r requirements.txt
```

## Run crawler
```bash
scrapy crawl bacalaureat -a year=2016 -a session=2 -o bacalaureat_2016.csv
```

### Spider arguments
`year` (optional) - any available year(from 2004 to present). If not specified it will take current year  
`session` (optional) - `1` for first session and `2` for September session


## Contribution
Feel free to contribute to this repo or give feedback. For more info contact me at [costin.bleotu@databus.systems](mailto:costin.bleotu@databus.systems).