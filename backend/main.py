import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(
    title='MTS_tst'
)

origins = [
    "http://localhost",
    "http://localhost:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/random')
async def get_random_dog():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = httpx.get(url)
    return json.load(response)


@app.get('/breed')
async def get_current_dog(breed: str):
    breed = breed.lower()
    if ' ' in breed:
        breed = '/'.join(reversed(breed.split(' ')))
    url = f'https://dog.ceo/api/breed/{breed}/images/random'
    response = httpx.get(url)
    return json.load(response)
