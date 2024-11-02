from fastapi import FastAPI,Request
import uvicorn

app=FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.delete("/delete_member/{crew_id}")
async def delete_member(crew_id:int):
    for member in crew:
        if member["id"]==crew_id:
            crew.remove(member)
            return{
                "msg":f" member with id number {crew_id} is deleted ops !",
                "members":crew
            }
    return {
        "msg":"memeber not found"
    }

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)