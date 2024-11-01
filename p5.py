from fastapi import FastAPI
import uvicorn

app=FastAPI()
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.get("/crew_path/{crew_id}") #user demande 
def read_crew_member_by_path(crew_id:int): # fonction fait le traitement a la base de ce que user demande
    for member in crew:                     # fonction pour chercher dans le backend ce que user chercher a partir sont interface 
        if member["id"]==crew_id:
            return member
    return {"msg " : "member not found"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
