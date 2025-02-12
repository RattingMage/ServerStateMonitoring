from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ServerStatus(BaseModel):
    cpu: int
    mem: str
    disk: str
    uptime: str

server_statuses = {
    1: {"cpu": 60, "mem": "30%", "disk": "43%", "uptime": "1d 2h 37m 6s"},
    2: {"cpu": 45, "mem": "25%", "disk": "50%", "uptime": "2d 5h 12m 34s"},
    3: {"cpu": 70, "mem": "40%", "disk": "60%", "uptime": "3d 8h 45m 12s"},
}

@app.get("/api/status/{server_number}", response_model=ServerStatus)
async def get_server_status(server_number: int):
    if server_number not in server_statuses:
        raise HTTPException(status_code=404, detail="Server not found")
    
    return server_statuses[server_number]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)