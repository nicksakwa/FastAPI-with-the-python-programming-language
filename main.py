from fastapi import FASTAPI
app= FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello, FasrAPI"}
@app.get("item/{item_id}")
async def read_item(item_id:int, query_param: str= None);
    return{"item_id":item_id, "query_param": query_param}