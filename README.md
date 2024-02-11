# Anki Decks

This repository provides a tool for creating Anki decks from JSON files. Follow the steps below to get started.

## Prerequisites

- Python 3.x installed on your machine
- Virtual environment tool (e.g., `venv` or `conda`) installed

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory: `cd anki-decks`.
3. Create a virtual environment: `python -m venv venv`.
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`.

## Usage

1. Place your JSON file(s) in the `json_decks` directory.
2. Run the following command in your terminal to generate the Anki deck:

```sh
python main.py json_decks/your_file_name.json
```
