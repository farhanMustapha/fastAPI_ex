from fastapi import FastAPI,Request
import uvicorn

app=FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.put("/crew_update/{crew_id}")
async def update_crew(crew_id:int,request:Request):
    data=await request.json()
    name=data["name"]
    role=data["role"]
    for member in crew:
        if member["id"]==crew_id:
            member["name"]=name
            member["role"]=role
            return {
                "crew_id":crew_id,
                "member":member
            }
    return {
            "msg":"not found"
        }

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
