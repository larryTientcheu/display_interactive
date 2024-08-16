# Display Interactive

This is a script that reads 2 files, customer data and purchase information. This script parses them and sends a payload to an API.
This project uses `python 3.12`

## Project Structure

```bash
.
├── .env
├── config.py
├── data
│   ├── customers.csv
│   └── purchases.csv
├── main.py
├── readme.md
├── requirements.txt
├── test_script.py
└── wrangle.ipynb
```

## Getting Started

* From the root of the repository, create a new python environment `.venv` using

```python
python -m venv .venv
```

* Make sure to select this environment as your working environment.
* For Unix Like Shells For Example Git Bash CLI., use

 ```sh
source .venv/bin/activate
```

* For Windows With CMD.

 ```cmd
.\.venv\Scripts\activate.bat
```

* For Windows With Power shell.

 ```powershell
.\.venv\Scripts\activate.ps1
```

* After creating the environment, install the necessary packages using the file `requirements.txt`.

 ```bash
pip install -r requirements.txt
```

* Do not forget to add the `.env` file with our `SECRETS`

## How to run

* To run this script, run the file `main.py` with some arguments. `dataset1.csv`, `dataset2.csv`
* Note that `customer` data should always be the first argument (`dataset 1`) and `purchases` data should be the second argument (`dataset 2`).
* The datasets can have any name as long as they are in the `data folder`

## Examples

* This runs the script.

 ```bash

  python main.py customers.csv purchases.csv

  ```

## Results

* After running the script successfully; log Information messages are displayed and a file app.log is created with all the logs

## Tests

* From the projects root, tests can be run using the command `pytest`

## Bonus

* For further interactivity, I implemented a python notebook `wrangle.ipynb` well documented, that shows all the data wrangling steps I took while working with the datasets.
* I decided to also provide the notebook because it is more visual friendly.
