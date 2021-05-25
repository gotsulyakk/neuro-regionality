# neuro-regionality

Generate funny ukrainian regional news with Markov chains  
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
## Generated examples
> Чоловік напився і бігав по парку з прапором нацистської Німеччини під час мітингу біля одеської ОДА.

> В Києві п'яний водій намагався свинею відкупитися від копів і виграти виснажливу погоню

> через відсутність маски Житель Одещини викрав жигуля і застряг на дереві.

> У Хмельницькому підрозділ ДСНС діставав з болота корову.

> У Дніпрі грабіжник заліз в будку охорони та підпалив її, щоб зігрітися.
