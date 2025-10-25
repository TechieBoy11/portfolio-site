# portfolio-site

## Requirements
All Requirements can be installed through requirements.txt
* flask
* Flask-Mail
* python-dotenv

## starting up
* CD to directory
* Use these commands to prepare the virtual environment
  ```
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```
* Create .env file with contents
  ```
  MAIL_USERNAME=your_email@gmail.com
  MAIL_PASSWORD=your_app_password
  ```
* Create a .gitignore file with the following
  ```
  # Ignore environment files
  .env

  # Python cache
  __pycache__/
  *.pyc

  # Virtual environment folders
  venv/
  env/

  # OS files
  .DS_Store
  Thumbs.db
  ```
* Start up the site with ```python app.py```


