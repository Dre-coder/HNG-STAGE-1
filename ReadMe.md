# Number Classification API

This is a FastAPI application that classifies numbers based on various properties such as prime, perfect, Armstrong, even/odd, and provides a fun fact about the number.

## Endpoints

### GET /api/classify-number

Classifies a number and returns its properties.

#### Parameters

- `number` (int | str): The number to classify. If a string is provided, an error response is returned.

#### Response

- `number` (int): The input number.
- `is_prime` (bool): Whether the number is prime.
- `is_perfect` (bool): Whether the number is perfect.
- `properties` (list): List of properties (e.g., "armstrong", "even", "odd").
- `digit_sum` (int): Sum of the digits of the number.
- `fun_fact` (str): A fun fact about the number from the Numbers API.

#### Example

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/classify-number?number=28' \
  -H 'accept: application/json'
  {
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even"],
  "digit_sum": 10,
  "fun_fact": "28 is the second perfect number."
}


