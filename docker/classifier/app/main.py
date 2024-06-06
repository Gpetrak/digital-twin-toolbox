from typing import Union

from fastapi import FastAPI, BackgroundTasks
import subprocess

app = FastAPI()


def first_command(input_file: str, output_file: str, model: str, color: str):
    
    # Define and run the command
    myprocess = subprocess.run(["../build/pcclassify", input_file, output_file, model, color], stdout=subprocess.PIPE)
    output = myprocess.stdout.decode('utf-8')
    return output

@app.post("/test/classifier/{query_id}")
async def test_command(query_id: int, background_tasks: BackgroundTasks):
    input_file = '/data/dataset-path/ML_models/test.laz'
    output_file = '/data/dataset-path/ML_models/test_class.laz'
    model = '/data/dataset-path/ML_models/modelV13_mono.bin'
    color = '--color'
    background_tasks.add_task(query_id, first_command, input_file, output_file, model, color)
    return {"message": "Your command is running with the ID: {}... Please wait for the response".format(query_id)}
