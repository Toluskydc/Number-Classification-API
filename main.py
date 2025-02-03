import os
import uvicorn
from fastapi import FastAPI, Query, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from mymath.my_math_lib import is_armstrong, is_perfect, is_perfect, is_prime, get_number_fact



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/classify-number", status_code=status.HTTP_200_OK)
async def classify_number(number: str = Query(...)):
    if not number.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={"number": "alphabet", "error": True}
        )
    
    number = int(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": get_number_fact(number),
    }




if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

