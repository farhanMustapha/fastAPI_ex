from fastapi import FastAPI
from fastapi import Request
import uvicorn



app=FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]


@app.post("/crew/")
async def add_crew_member(request:Request): # je suis le serveur je vais recevoir la requete ,je doit la analyser cad voir le contenu le separer sur des variable 
    data=await request.json()
    name=data["name"]
    role=data["role"]

    crew_id= max(member["id"] for member in crew)+1 if crew else 1
    
    """
    autre facon 
    if crew:
        max_id=max(member["id"] for member in crew)
        new_id=max_id+1
    else:
            new_id=1 """

    #print(crew_id)
    new_member={"id":crew_id,"name":name,"role":role}
    crew.append(new_member)

    msg=f"Welcome to the crew {name}!"

    return {
        "msg":msg,
        "crew_id":crew_id,"new_member":new_member
        }


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)