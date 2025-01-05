from fastapi import FastAPI, Depends, HTTPException
from models import User
from typing import List
from db import init_db
from routes.user import router as userrouter
from routes.job import router as jobrouter
from typing import Annotated
from fastapi.security import OAuth2AuthorizationCodeBearer
from jwt import PyJWKClient
import jwt
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

origins = [
    "http://localhost:8080",
    "http://keycloak:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth_2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl= os.environ.get("TOKEN_URL", default="http://keycloak:8080/realms/cloudplatforms/protocol/openid-connect/token"),
    authorizationUrl=os.environ.get("AUTH_URL", default="http://keycloak:8080/realms/cloudplatforms/protocol/openid-connect/auth"),
    refreshUrl=os.environ.get("REFRESH_URL", default="http://keycloak:8080/realms/cloudplatforms/protocol/openid-connect/auth")
)



async def valid_access_token(
    access_token: Annotated[str, Depends(oauth_2_scheme)]
):
    url = os.environ.get("CERT_URL", default="http://keycloak:8080/realms/cloudplatforms/protocol/openid-connect/certs")
    optional_custom_headers = {"User-agent": "custom-user-agent"}
    jwks_client = PyJWKClient(url, headers=optional_custom_headers)

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(access_token)
        print('signing_key')
        print(signing_key)
        data = jwt.decode(
            access_token,
            signing_key.key,
            algorithms=["RS256"],
            audience="account",
            options={"verify_exp": True},
        )
        print('data')
        print(data)
        return data
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Not authenticated")


@app.on_event("startup")
async def startup():
    await init_db()



@app.get("/private", dependencies=[Depends(valid_access_token)])
def get_private():
    return {"message": "Ce endpoint est privé"}

app.include_router(userrouter, prefix="/user", tags=["User"])
app.include_router(jobrouter, prefix="/job", tags=["Job"])
