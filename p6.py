from fastapi import FastAPI
import uvicorn

app = FastAPI()
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.get("/crew_path/{crew_id}/{role}")
def read_crew_member_by_path(crew_id: int, role: str):
    for member in crew:
        if member["id"] == crew_id and member["role"].upper() == role.upper():
            #fait attetion avec les majuscul 
            return member
    return {"msg": "Member not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
