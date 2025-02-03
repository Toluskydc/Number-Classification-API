# Number Classification API

## Project Description
This API classifies a given number based on mathematical properties such as being prime, perfect, Armstrong, odd, or even. It also provides a fun fact about the number using the Numbers API.

## Features
- Accepts a number as a query parameter.
- Determines if the number is prime, perfect, or an Armstrong number.
- Computes the sum of the digits of the number.
- Fetches a fun fact about the number from the Numbers API.
- Handles errors appropriately.
- Implements CORS to allow cross-origin requests.
- Returns results in JSON format.

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Requests (for fetching fun facts from the Numbers API)

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/Toluskydc/Number-Classification-API.git
cd Number-Classification-API
```

### Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Application
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API Documentation
Once the server is running, you can access interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Specification

### Endpoint: GET `/api/classify-number?number={number}`

#### Request Parameters
- `number` (integer): The number to classify.

#### Example Request
```sh
GET /api/classify-number?number=371
```

#### Successful Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)
If the input is not a valid integer, the response will be:
```json
{
    "number": "alphabet",
    "error": true
}
```

## Deployment
The API is deployed on **Render** and can be accessed publicly.



