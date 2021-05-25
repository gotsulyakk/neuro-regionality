# neuro-regionality

Generating funny ukrainian news with Markov chains
Data parsed from https://t.me/regionality

## Installation

Python >= 3.6

```sh
cd neuro-regionality
pip install requirements.txt
```
## Usage
Register at https://my.telegram.org/apps
Add your unique variables to config.ini

Command below will generate 1 sentence containing max 100 characters
```sh
python generate_msg.py --sentences=1 --max_chars=100
```
