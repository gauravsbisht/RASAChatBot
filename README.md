# RASAChatBot
This is a restaurant Chatbot build using Open Source Conversational AI - RASA 1.10.3
## Objective
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience
Conversation Chatbot

## Following are the installation steps
### Requirements:

1. Python (requires Python 3.6.0 or higher)

For Windows:
Use the following code and check whether your Python environment is already installed:
```
$ python3 --version
If not, then install it using
C:\> pip3 install -U pip
```
For macOS:
Before installing Python, you have to install the Homebrew package manager if you haven’t already. Use the following code to do so:
```
$ brew update
$ brew install python
``` 

2. Visual Studio: (For Windows only)
Open the Microsoft Visual Studio link: https://visualstudio.microsoft.com/downloads/
Select ‘Community version 2019’
Download the installer and select VC++ Build tools on the list


3. Creating a virtual environment
We strongly recommend that you create a virtual environment before installing Rasa and Rasa X.
Virtual environment tools like virtualenv and virtualenvwrapper provide isolated Python environments. They help you install packages without any dependency conflicts and root privileges.

For Windows:
You can create a virtual environment by opening the command prompt and typing the following code:
```
C:\> python3 -m venv --system-site-packages ./venv
You can activate the virtual environment by typing the following code:
C:\> .\venv\Scripts\activate
```

For macOS:
You can create the virtual environment by opening the command prompt and typing the following code:
```
$ python3 -m venv --system-site-packages ./venv
You can activate the virtual environment by typing the following code:
$ source ./venv/bin/activate
```

4. Installing Rasa and Rasa X:

You can install both Rasa and Rasa X using the following code:
```
$ pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
Use the following code only if you want to install Rasa:
$ pip install rasa 
```


5. Install Rasa NLU and Spacy in the same command prompt:
```
$ pip install rasa[spacy]
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en
``` 
Note: If the system prompts you to upgrade pip, then use the following commands:
For Windows:

```
python -m pip install --upgrade pip
``` 
For macOS:
```
pip install pip –upgrade
pip install setuptools –upgrade
```


The bot is trained using 
```
rasa train 
```
and executed using 
```
rasa shell
```
