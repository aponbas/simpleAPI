from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from security import authenticate_user, create_access_token, get_current_user, register_user
from typing import Annotated
from User import User


app = FastAPI()


@app.get("/")
def server_status() -> str:
    """Liveliness tester, returns "I'm alive!" when the server is on. No authentication needed."""
    return "I'm alive!"


@app.post("/register")
async def register(user: User):
    """Register a new user. Only username and password as input right now."""
    register_user(user)
    return status.HTTP_201_CREATED


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Retrieve a token based on the user's login. The token can be used for 30 minutes."""
    user = authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/test_call")
async def call_request(current_user: Annotated[User, Depends(get_current_user)]):
    """Sample call. If the request has a valid token, it'll respond with the username. If not, it gives a
    not-authenticated error."""
    return f"Je bent ingelogd, {current_user.username}."
