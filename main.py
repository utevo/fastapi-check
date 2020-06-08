from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {'message': "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'id': item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def read_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 1}
    elif model_name == ModelName.resnet:
        return {'model_name': model_name, 'message': 2}
    elif model_name == ModelName.lenet:
        return {'model_name': model_name, 'message': 3}
        