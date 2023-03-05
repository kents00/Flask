![Flask_Template](https://user-images.githubusercontent.com/69900896/222946903-44da38fe-a041-4193-acde-52c9bbfa72c5.png)

# Flask

A simple flask template for beginners creating a simple project reference

## Setup

To deploy this flask project just install a `virtual environment` on your computer

### Ubuntu LTS ≤ 20.04

Installing pip

```bash
sudo apt-get install python3-pip
```

Installing virtual environment using pip3

```bash
sudo pip3 install virtualenv
```

Creating virtual environment

```bash
virtual env
```

Activate virtual environment

```
source env/bin/activate
```

Deactivate

```
deactivate
```

### Windows

Installing pip

```
python -m pip install --user --upgrade pip

```

Installing virtual environment using pip

```
pip install virtualenv

```

Creating virtual environment

```
virtual
```

Deactivate

```bash
deactivate
```

## MacOS

For macOS, you can install pip by downloading the [get-pip.py](https://bootstrap.pypa.io/get-pip.py) script and running it with Python 3:

```
curl <https://bootstrap.pypa.io/get-pip.py> -o get-pip.py
python3 get-pip.py

```

Then, you can install virtualenv using pip3:

```
pip3 install virtualenv

```

After installing virtualenv, you can create and activate a virtual environment as follows:

```
virtualenv env
source env/bin/activate
```

To deactivate the virtual environment, simply run:

```
deactivate
```

Finally, install Flask using pip3:

```
pip3 install flask
```

## Installation

When installing packages in this project, type the following:

```bash
pip install -r requirements.txt
```

## Run Flask

To run the Flask application, set the FLASK_APP environment variable to the name of your Flask application file and then run the following command:

```
flask run
```
