from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

[
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 181.98,
    "uptime_pct": 99.146,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 117.92,
    "uptime_pct": 97.538,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 173.51,
    "uptime_pct": 97.158,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 220.72,
    "uptime_pct": 99.442,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 163.49,
    "uptime_pct": 99.085,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 175.15,
    "uptime_pct": 99.212,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 159.86,
    "uptime_pct": 98.889,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 217.95,
    "uptime_pct": 98.235,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 136.77,
    "uptime_pct": 97.635,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 131.32,
    "uptime_pct": 97.603,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 126.7,
    "uptime_pct": 99.482,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 164.56,
    "uptime_pct": 98.766,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 223.22,
    "uptime_pct": 97.65,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 204.38,
    "uptime_pct": 99.265,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 138.56,
    "uptime_pct": 98.331,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 216.94,
    "uptime_pct": 97.388,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 173.63,
    "uptime_pct": 98.759,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 223.66,
    "uptime_pct": 97.462,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 175.46,
    "uptime_pct": 99.175,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 215.47,
    "uptime_pct": 99.031,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 133.07,
    "uptime_pct": 99.165,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 102.56,
    "uptime_pct": 98.721,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 162.06,
    "uptime_pct": 98.75,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 110.24,
    "uptime_pct": 97.922,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 190.07,
    "uptime_pct": 97.56,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 141.73,
    "uptime_pct": 97.701,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 231.22,
    "uptime_pct": 99.188,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 100.91,
    "uptime_pct": 98.402,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 233.14,
    "uptime_pct": 97.842,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 163.71,
    "uptime_pct": 97.127,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 130.68,
    "uptime_pct": 97.139,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 201.92,
    "uptime_pct": 98.474,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 164.18,
    "uptime_pct": 98.601,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 198.57,
    "uptime_pct": 97.714,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 154.71,
    "uptime_pct": 97.841,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 116.89,
    "uptime_pct": 98.969,
    "timestamp": 20250312
  }
]
TELEMETRY_DATA = json.loads("""
[
  {"region": "apac", "service": "support", "latency_ms": 147.13, ...},
  ...  ← your 36 rows go here
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}