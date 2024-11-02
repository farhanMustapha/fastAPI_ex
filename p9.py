from fastapi import FastAPI
import asyncio  # Used to delay for 2 seconds
import uvicorn

app = FastAPI()


crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]



@app.get("/crew_async")
async def get_all_member():
    await asyncio.sleep(2)
    return {
        "msg":"all data",
        "data":crew
    }

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8080)
    