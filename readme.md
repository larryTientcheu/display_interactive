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

* Make sure to select this virtual environment as your working environment.
  
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

* After creating the environment and selecting it, install the necessary packages using the file `requirements.txt`.
  
  ```bash
  pip install -r requirements.txt
  ```

## Environment Variables

* The default environment is `development`, explicitly set the environment variable `ENV` to `prod` for `production` and `stage` for `staging`.
  
  ```python
  ENV="prod" or ENV="stage"
  ```

* To set the Url, use the environment variables
  
  ```python
  # the url string here is an example
  DEV_CLOUD_API_URL="dev.url.com" # for development
  PROD_CLOUD_API_URL="prodserver.api.com" # for production
  STAGE_CLOUD_API_URL="stageinfra.address.com" # for staging
  ```

* To set the environment variables, `VARNAME` here is the actual environment variable name as shown in capital letters above.
  * UNIX

    ```bash
    export VARNAME=value
    ```

  * Windows

    ```cmd
    set VARNAME=value
    ```

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
