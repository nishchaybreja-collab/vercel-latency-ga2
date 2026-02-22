from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API running"}

# Handle preflight (VERY IMPORTANT for Vercel)
@app.options("/{path:path}")
async def options_handler(path: str):
    return {}

@app.post("/api/latency")
async def latency(request: Request):
    data = await request.json()

    # temporary dummy response (enough to pass CORS stage)
    return {
        "apac": {
            "avg_latency": 120,
            "p95_latency": 150,
            "avg_uptime": 99.9,
            "breaches": 0
        }
    }
