from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def index():
    return JSONResponse(
        content = {
            "ok": True,
            "code": 200,
            "data": {"versioin": "1.0.0"},
            "message": "Success"
        }
    )

from routes import cleansing
app.include_router(cleansing.router, tags=["Cleansing"])
