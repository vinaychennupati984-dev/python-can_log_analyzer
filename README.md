# Python CAN Log Analyzer

A Python-based automation tool for parsing CAN logs, decoding signals using DBC files, validating signal limits, and generating XML test reports.

This project demonstrates how Python can be used to automate CAN log analysis in embedded and automotive testing environments.

---

## Features

- CAN log parsing
- DBC-based signal decoding
- Signal validation using min/max limits
- XML report generation
- Automation logging

---

## Technologies Used

- Python
- cantools (DBC decoding)
- XML (test report generation)
- Logging module

---

## Project Structure

can-log-analyzer
│
├── main.py
├── log_parser.py
├── dbc_decoder.py
├── validator.py
├── report_generator.py
├── logger.py
│
├── vehicle.dbc
├── sample_log.txt
├── requirements.txt
└── README.md


---

## How It Works

1. Parse CAN log file
2. Decode CAN frames using DBC
3. Extract signal values
4. Validate signals using defined ranges
5. Generate XML report with results


---

## How It Works

1. Parse CAN log file
2. Decode CAN frames using DBC
3. Extract signal values
4. Validate signals using defined ranges
5. Generate XML report with results



---

## Installation

Install required library:
pip install cantools

## Running the Project

Run the main script:


python main.py


After execution, the tool will generate:

- `report.xml` – XML test report
- `automation.log` – execution logs

---

## Example Output


Example decoded signals:


Speed = 50 km/h
Temperature = 80 C


Example XML report:

```xml
<TestReport>
  <Signals>
    <Frame>
      <Speed>50</Speed>
      <Temperature>80</Temperature>
    </Frame>
  </Signals>
</TestReport>

Use Case

This project demonstrates automation of CAN log analysis commonly performed during ECU validation and automotive testing.

Future Improvements

Support multiple CAN log formats

Signal frequency validation

Missing signal detection

Integration with automated test frameworks

Author

Vinay Chandra

Embedded Software Engineer transitioning to Python Automation.