from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import requests

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
def is_perfect(n):
    if n<=1:
         return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
    
def sum_digits(n):
    sum = 0
    for i in str(n):
        sum+=int(i)
    return sum   

def get_armstrong(n):
    armstrong = 0
    for i in str(n):
        armstrong+= int(n)**3
    if armstrong == n:
        return True
    return False

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def properties(n):
    armstrong = get_armstrong(n)
    even = is_even(n)
    if armstrong:
        if even:
            return ["armstrong", "even"]
        return["armstrong", "odd"]
    if even:
        return ["even"]
    return["odd"]

        
app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: int | str):
    if type(number)==type("hi"):
        return JSONResponse(content={
            "number": number,
            "error": True
        }, status_code=status.HTTP_400_BAD_REQUEST)

    response =  requests.get(f"http://numbersapi.com/{number}/math")
    print(response.text)
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties(number),
        "digit_sum": sum_digits(number),
        "fun_fact": response.text 
    } 