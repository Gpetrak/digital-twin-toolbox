from typing import Union

from fastapi import FastAPI, BackgroundTasks
import subprocess

app = FastAPI()

'''
@app.get("/")
def read_root():
    return {"Hello": "Big world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
'''

def first_command(cmd: str):
    return subprocess.run(cmd)

@app.get("/test/{cmd}")
async def test_command(cmd: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(first_command, cmd)
    return {"message": "test command sent in the background"}
