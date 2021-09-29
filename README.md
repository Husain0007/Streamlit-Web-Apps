# Streamlit-Web-Apps
[Streamlit](https://streamlit.io/) is an Python package built with the idea of simplifying the process of making a Web-App.

 ## Virtual Enviornment Setup
 Below are instructions to installing [Pipenv](https://realpython.com/pipenv-guide/) a python packaging tool that helps create and manage virtual enviornments.

### Updating `pip`
Type the following in terminal
```
python3.8 -m pip install pip --upgrade
```
### Installing `Pipenv` globally
```
python3.8 -m pip install pipenv
```
### Verify installation
```
pipenv
```
### Initializing Virtual Enviornment with `Pipenv`
In the terminal navigate to your project directory.
```
pipenv install --python 3.8
```
### Activate the Virtual Enviornment
```
pipenv shell
```

### Install dependencies
```
pip install -r requirements.txt
```

### Deactivate the Virtual Enviornment
```
exit
```

## Running Web App
```
streamlit run file.py
```

