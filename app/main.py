
from typing import Optional

from fastapi import FastAPI

import docker

app = FastAPI()
# dockerClient = docker.APIClient(base_url='unix://var/run/docker.sock')
dockerClient = docker.from_env()


@app.get("/")
def info():
    return "Docker REST API"

@app.get("/status")
def check_status():
    return {"Status": "OK"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/docker")
async def docker():
    dockerVer = dockerClient.version()
    # print(dockerVer)
    return dockerVer
    
@app.get("/docker-ping")
async def docker_ping():
    return dockerClient.ping()

@app.get("/containers")
async def get_containers():
    containers = dockerClient.containers.list()
    return containers

@app.get("/images")
async def get_images():
    images = dockerClient.images.list()
    return images
