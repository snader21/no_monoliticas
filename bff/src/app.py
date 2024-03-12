from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from endpoints.v1 import endpoints

# create the app object
app = FastAPI()

# Includes the endpoints in the app
app.include_router(endpoints.router)
