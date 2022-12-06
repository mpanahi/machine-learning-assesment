# Line-up extraction Service

## Summary
The purpose of this app is to extract line_up from events.

## Project structure

- `data`: contains files artists.txt, which is the list of available artists.
event_titles.txt, which is the sample of events for testing.
- `src`: contains the files necessary for named entity recognition and two other files. solution.py, which is the main algorithm for extracting line-ups and confidence of extraction for each.
simple_api.py, which is the FastAPI implementation for the algorithm.

## Installation

Verify the python version installed. This project was built using python 3.7
```
python --version
```

Activate the virtualenv
```
pipenv shell --python 3.7
```

Install project dependencies requirement.txt
```
pip3 install -r requirements.txt
```
## Usage

To run the app localy, go to the root and then src directory and run:
```
uvicorn simple_api:app --reload
```
you can visit http://localhost:8000/docs to see your API docs.



