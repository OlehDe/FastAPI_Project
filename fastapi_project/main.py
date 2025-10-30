from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#pip install fastapi uvicorn
#fastapi dev main.py
#https://app.diagrams.net/#G1Kbk6UIWjM-8sHL1Qv3co49U7IwJ7ygUA#%7B%22pageId%22%3A%22w7UQazSxdPBglzHmsAxP%22%7D