import os
import uvicorn
from fastapi import FastAPI, Query, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from mymath.my_math_lib import is_armstrong, is_perfect, is_perfect, is_prime, get_number_fact
from fastapi.responses import JSONResponse



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/classify-number")
async def classify_number(number: str = Query(...)):
    if not number.lstrip('-').isdigit():
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True} 
        )
    num = int(number)
    properties = ["even" if num % 2 == 0 else "odd"]
    if is_armstrong(num):
        properties.insert(0, "armstrong")

    prime_status = is_prime(num)
    perfect_status = is_perfect(num)

    return {
        "number": num,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(num))),
        "fun_fact": get_number_fact(num)
    }



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

