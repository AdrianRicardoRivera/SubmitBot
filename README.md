# SubmitBot

SubmitBot is a script that takes a project name and file paths as arguments and automatically submits them to gradescope.com for CMSC330.

## Installation

Place the SubmitBot directory in the parent directory holding your project directories.

Within the SubmitBot directory there is an example submit.sh script. This script should be copied into your project directory and edited to include the project name (as listed in gradescope) and the relative path to the submission files.

```bash
source ../SubmitBot/venv/bin/activate
python3 ../SubmitBot/submit.py PROJECTNAME FILE1 FILE2 ...
deactivate
```

Example

```bash
source ../SubmitBot/venv/bin/activate
python3 ../SubmitBot/submit.py P3 src/nfa.ml src/regexp.ml
deactivate
```
Remember to add your username and password into the credentials.py file.

```python
username = 'USERNAME'
password = 'PASSWORD'
```

## Usage

Run the script to submit your files.

```bash
sh submit.sh
```

To use with another project simply copy submit.sh to the new project directory and edit the project name and files.
