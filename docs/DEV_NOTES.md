# DEV NOTES
## Sample Directory Structures
### Python Repo Structure Sample:
```
helloworld/
│
├── sample/
│   ├── __init__.py
│   ├── core.py
│   └── helpers.py
│
├── docs/
│   ├── conf.py
│   └── index.rst
│
├── tests/
│   ├── test_basic.py
│   └── test_advanced.py
│
├── .gitignore
├── README.rst
├── LICENSE
├── setup.py
└── requirements.txt
```

### CLI Application w/ Internal Packages:
```
helloworld/
│
├── bin/
│   └── helloworld(.py or .sh)
│
├── docs/
│   ├── hello.md
│   └── world.md
│
├── helloworld/
│   ├── __init__.py
│   ├── runner.py
│   ├── hello/
│   │   ├── __init__.py
│   │   ├── hello.py
│   │   └── helpers.py
│   │
│   └── world/
│       ├── __init__.py
│       ├── helpers.py
│       └── world.py
│
├── data/
│   ├── input.csv
│   └── output.xlsx
│
├── tests/
│   ├── hello
│   │   ├── helpers_tests.py
│   │   └── hello_tests.py
│   │
│   └── world/
│       ├── helpers_tests.py
│       └── world_tests.py
│
├── .gitignore
├── LICENSE
└── README.md
```

### CLI Installable:
```
helloworld/
│
├── helloworld/
│   ├── __init__.py
│   ├── helloworld.py
│   └── helpers.py
│
├── tests/
│   ├── helloworld_tests.py
│   └── helpers_tests.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

### Dead Simple Python Project Structure:
```
omission-git
├── LICENSE.md
├── omission
│   ├── app.py
│   ├── common
│   │   ├── classproperty.py
│   │   ├── constants.py
│   │   ├── game_enums.py
│   │   └── __init__.py
│   ├── data
│   │   ├── data_loader.py
│   │   ├── game_round_settings.py
│   │   ├── __init__.py
│   │   ├── scoreboard.py
│   │   └── settings.py
│   ├── game
│   │   ├── content_loader.py
│   │   ├── game_item.py
│   │   ├── game_round.py
│   │   ├── __init__.py
│   │   └── timer.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── resources
│   └── tests
│       ├── __init__.py
│       ├── test_game_item.py
│       ├── test_game_round_settings.py
│       ├── test_scoreboard.py
│       ├── test_settings.py
│       ├── test_test.py
│       └── test_timer.py
├── pylintrc
├── README.md
└── .gitignore
```
