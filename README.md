# Python CAN Log Analyzer

Python automation tool for analyzing CAN logs and validating ECU signals.

## Features

- CAN log parsing
- DBC signal decoding
- YAML configuration
- CLI execution
- XML test report generation
- logging
- unit testing using pytest

## Architecture

           +--------------+
           |   CAN LOG    |
           +--------------+
                    |
                    v
           +--------------+
           |  Log Parser  |
           +--------------+
                    |
                    v
           +--------------+
           |  DBC Decoder |
           +--------------+
                    |
                    v
           +--------------+
           | Signal Check |
           +--------------+
                    |
                    v
           +--------------+
           |  XML Report  |
           +--------------+

## Run Tool

python main.py

## Override inputs

python main.py --log custom_log.txt --dbc custom.dbc

## Run Tests

pytest