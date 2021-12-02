"""vim debug smple"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost", "http://localhost:5000"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_headers(req: Request):
    """return client headers"""
    client_headers = req.headers
    return {"headers": client_headers}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
