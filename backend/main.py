from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math, random

app = FastAPI(title="3D Particle Form Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ShapeRequest(BaseModel):
    shape: str = "sphere"
    points: int = 10000

@app.get("/")
def root():
    return {"ok": True, "service": "3D Particle Form Studio API"}

@app.post("/point-cloud")
def point_cloud(req: ShapeRequest):
    n = max(100, min(req.points, 100000))
    shape = req.shape.lower().strip()
    points = []

    if shape == "sphere":
        for _ in range(n):
            u = random.uniform(-1, 1)
            a = random.uniform(0, math.tau)
            s = math.sqrt(1-u*u)
            r = 3.5
            points.append([r*s*math.cos(a), r*u, r*s*math.sin(a), .45, .08, 1.0])

    elif shape == "torus":
        for _ in range(n):
            u, v = random.uniform(0, math.tau), random.uniform(0, math.tau)
            R, r = 3.0, 1.15
            points.append([
                (R+r*math.cos(v))*math.cos(u),
                r*math.sin(v),
                (R+r*math.cos(v))*math.sin(u),
                .05, .8, 1.0
            ])
    else:
        return {"error": "Backend demo currently exposes sphere and torus. Frontend handles text, emoji, car, heart and star."}

    return {"shape": shape, "count": len(points), "points": points}
