from fastapi import FastAPI
import uvicorn


app=FastAPI() 

crew = [ # notre base de donne
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]
@app.get("/crew")
def home(): #cette fonction permet de reterner tout ce que on a dans la base de donne
    return {"message":"Succes","data":crew}
        
    
        

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8001) # permet de demarer le server