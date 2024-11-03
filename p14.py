from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn

app=FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain", "experience": 10},
    {"id": 2, "name": "Alice", "role": "Engineer", "experience": 8},
    {"id": 3, "name": "Bob", "role": "Scientist", "experience": 5}
]

class CrewMember(BaseModel):
    name:str
    role:str
    experience:int

@app.get("/crew/{crew_id}",response_model=CrewMember)
async def get_member(crew_id:int):
    for m in crew:
        if m["id"]==crew_id:
            return {"data":m}
    return {"msg":"element not found"}




if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)