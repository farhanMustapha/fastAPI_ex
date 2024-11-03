from fastapi import FastAPI
from fastapi import Request
import uvicorn

app=FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]


@app.get("/")
async def get_all():
        if crew:
           for m in crew:
                return {"data":m}
        else:
             return{"data":"list vide"}
           
         

@app.get("/crew/{crew_id}")
async def read_crew_member(crew_id:int):
      for m in crew:
           if m["id"]==crew_id:
                return {
                     "crew_id":crew_id,
                     "m":m
                     }
      return {"msg":"element not found"}

@app.post("/crew")
async def add_crew_member(request:Request):
     data=await request.json()
     name=data["name"]
     role=data["role"]
     new_id=max(member["id"] for member in crew)+1 if crew else 1
     new_member={"id":new_id,"name":name,"role":role}
     crew.append(new_member)
     return {"new_member":new_member}


@app.put("/crew_update/{crew_id}")
async def update_member(crew_id:int,request:Request):
     data=await request.json()
     name=data["name"]
     role=data["role"]
     for m in crew:
          if m["id"]==crew_id:
               m["name"]=name
               m["role"]=role
               return {"m":m}
     return {"msg":"element not found"}

@app.delete("/crew/{crew_id}")
async def delete_crew(crew_id:int):
     for m in crew:
          if m["id"]==crew_id:
               crew.remove(m)
               return {"crew":crew}
     return {"msg":"crew member not found"}
     

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)