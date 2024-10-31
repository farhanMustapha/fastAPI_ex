from fastapi import FastAPI
import uvicorn


app=FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]
@app.get("/crew")
def home():
    return [
        {"message":"Succes"},
        {"data":crew}
        
    ]
        

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8001)