import json
import redis
from typing import Callable
from datetime import timedelta
from fastapi import FastAPI, HTTPException
from aiobreaker import CircuitBreaker
from aiobreaker.storage import CircuitRedisStorage
from aiobreaker.state import CircuitBreakerState, CircuitBreakerError

app = FastAPI()
redis_storage = CircuitRedisStorage(
    state=CircuitBreakerState.OPEN,
    redis_object=redis.Redis(host="127.0.0.1", port=6379, db=0),
    namespace="aiobreaker",
    fallback_circuit_state=CircuitBreakerState.CLOSED,
)


@CircuitBreaker(fail_max=5, timeout_duration=timedelta(seconds=60), state_storage=redis_storage)
async def get_item(item_id: int):
    items = {1: "Product"}
    return items[item_id]


@app.get("/")
async def read_item(item_id: int):
    try:
        return await get_item(item_id)
    except CircuitBreakerError:
        return "open"
    except Exception as e:
        print(e)
        return HTTPException(status_code=404, detail="Item not found")