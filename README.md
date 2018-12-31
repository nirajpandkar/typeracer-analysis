# TypeRacer Race and Text Analysis

> Exploratory data analysis on my personal race data as well as site wide text data.

## Installation

* Install dependencies

```bash
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

**Note**: Requires only a second for my races to download since there are only over 4000 races, but someone like deroche1 who has over 250,000 races would require more time. (Took me a minute and a half to download. You can find that user's data in the 'data' folder.)
All the analysis has been done on my race data.

* Clean and normalize the raw data

```bash
python clean_and_normalize.py
```

* Cleaned data will be available in 'data' folder. Use the notebooks for further analysis.

