# Setting up your local server

1. Create a venv `python -m venv .\venv`
2. Activate venv `.\venv\Scripts\activate`
3. Run `pip install -r requirements.txt`
4. Run `gcloud auth application-default login`
   
# Running your local server
1. Activate venv with `.\venv\Scripts\activate`
2. Run `python src/run.py`
3. See the API documentation at [127.0.0.1:8000/docs](127.0.0.1:8000/docs)
You can register a user without authenticating (ofcourse).
After authenticating, click "Authorize" in the top right corner and fill in your username and password.
It is not necessary to add any scopes.
An application can use the /token endpoint, also here only the username and password are required.
The response will contain a token that can be used for the other endpoints.

# Deploy to Google Cloud Platform
For the first deployment, follow these steps:
1. Create app.yaml file in /src and fill in variables (see template)
2. Run `gcloud auth login`

For future deployments, follow only the next steps:
1. Run `gcloud app deploy src/app.yaml`
2. See API documentation at [oose-simple-api.ew.r.appspot.com/docs](oose-simple-api.ew.r.appspot.com/docs)
