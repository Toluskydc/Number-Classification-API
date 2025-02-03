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


@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"number": "alphabet", "error": True}
    )


# @app.get("/api/classify-number", status_code=status.HTTP_200_OK)
# async def classify_number(number: str = Query(...)):
#     if not number.isdigit():
#         raise ValueError("Invalid number")
    
#     number = int(number)
#     properties = []
#     if is_armstrong(number):
#         properties.append("armstrong")
#     properties.append("odd" if number % 2 else "even")
    
#     return {
#         "number": number,
#         "is_prime": is_prime(number),
#         "is_perfect": is_perfect(number),
#         "properties": properties,
#         "digit_sum": sum(int(d) for d in str(number)),
#         "fun_fact": get_number_fact(number),
#     }




# @app.get("/api/classify-number")
# async def classify_number(number: str = Query(...)):
#     """Classifies the given number"""
#     if not number.lstrip('-').isdigit():  # Allow negative numbers
#         raise ValueError("Invalid number")  
    
#     num = int(number)

#     # Classify even/odd
#     properties = ["even" if num % 2 == 0 else "odd"]

#     # Check Armstrong property
#     if is_armstrong(num):
#         properties.insert(0, "armstrong")  # Keep order consistent

#     return {
#         "number": num,
#         "is_prime": False,  # (You may want to implement prime checking)
#         "is_perfect": False,  # (Implement perfect number check if needed)
#         "properties": properties,
#         "digit_sum": sum(int(d) for d in str(abs(num))),  # Sum of digits
#         "fun_fact": get_number_fact(num)  # Get fun fact from the separate function
#     }


# @app.get("/api/classify-number")
# async def classify_number(number: str = Query(...)):
#     """Classifies the given number"""
#     if not number.lstrip('-').isdigit():  # Allow negative numbers, reject non-numeric input
#         return JSONResponse(
#             status_code=400,
#             content={"number": number, "error": True}  # Return the exact invalid input
#         )

#     num = int(number)

#     # Classify even/odd
#     properties = ["even" if num % 2 == 0 else "odd"]

#     # Check Armstrong property
#     if is_armstrong(num):
#         properties.insert(0, "armstrong")  # Keep order consistent

#     return {
#         "number": num,
#         "is_prime": False,  # Implement prime checking if needed
#         "is_perfect": False,  # Implement perfect number check if needed
#         "properties": properties,
#         "digit_sum": sum(int(d) for d in str(abs(num))),  # Sum of digits
#         "fun_fact": get_number_fact(num)  # Fetch fun fact
#     }



@app.get("/api/classify-number")
async def classify_number(number: str = Query(...)):
    """Classifies the given number"""
    if not number.lstrip('-').isdigit():  # Allow negative numbers, reject non-numeric input
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True}  # Return the exact invalid input
        )

    num = int(number)

    # Classify even/odd
    properties = ["even" if num % 2 == 0 else "odd"]

    # Check Armstrong property
    if is_armstrong(num):
        properties.insert(0, "armstrong")  # Keep order consistent

    return {
        "number": num,
        "is_prime": False,  # Implement prime checking if needed
        "is_perfect": False,  # Implement perfect number check if needed
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(num))),  # Sum of digits
        "fun_fact": get_number_fact(num)  # Fetch fun fact
    }



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

