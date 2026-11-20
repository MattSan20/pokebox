# POKEBOX APP

a small python app that manages your pokemon team and pc storage, this is based on how the system actually works in the game. You can holdup to 6 pokemon in your personal team and when that team is full everything else will go to your pc storage which is 30 slots.

## TECH

- Python 3.12
- pytest (tests) + pytest-cov (coverage)
- GitHubActions + SonarQube Cloud

## SETUP

pip install - r requirements.txt
pip install -e .

# HOW TO USE (Some Commands)

```
pokebox add Psyduck --level 10 -- types Water -- nickname Headache
pokebox team
pokebox deposit Psyduck
pokebox pc
```

## Run tests

```
pytest --cov=src --cov-report=term
```
