# 3D Particle Form Studio

## Fastest way to run the working visual version

1. Install Python if it is not already installed.
2. Double-click `run_frontend.bat`.
3. Open `http://localhost:8000/frontend/` in Chrome or Edge.
4. Keep internet access enabled because Three.js is loaded from jsDelivr.

Try:
- A
- HELLO
- ❤️
- 🔥
- CAR
- HEART
- STAR
- SPHERE
- TORUS

Drag the viewport to rotate and use the mouse wheel to zoom.

## Optional Python API

The included FastAPI backend is the beginning of the Python/AI/point-cloud layer.

Double-click `run_backend.bat`.

API:
- GET http://localhost:8001/
- POST http://localhost:8001/point-cloud

The browser demo intentionally generates its built-in shapes locally so it works even if the backend is not running.

## Architecture

Frontend: HTML/CSS/JavaScript + Three.js/WebGL
Backend foundation: Python + FastAPI
Future arbitrary-object layer: 3D asset/text-to-3D service -> point-cloud converter -> browser particle renderer

Important: arbitrary objects such as "elephant" or "Ferrari" require a 3D model/AI asset source. No browser-only program can infer an accurate arbitrary 3D mesh from the word alone without such a model/service.
