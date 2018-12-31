# TypeRacer Race and Text Analysis

> Exploratory data analysis on my personal race data as well as site wide text data.

## Installation

* Install dependencies
```
pip install -r requirements.txt
```

## Usage

* Download all the texts used on the site

```bash
python scrape_texts.py
```

* Download all the races of a particular user

```bash
python scrape_races.py -u nirajp
```

* Clean and normalize the raw data

```bash
python clean_and_normalize.py
```

* Cleaned data will be available in 'data' folder. Use the notebooks for further analysis.

