1. python -m venv myenv
myenv\Scripts\activate
pip install fastapi uvicorn pydantic    
uvicorn main:app --reload
----------------------------------------
path parameters  - Path parameter ka matlab hai: URL ke andar kisi specific item ki value dena.

isme 5 dynamic/variable hai jo ek specific resource ko allocate karta hai humare server ko

ex - localhost:8000/product/5
{id}->5 i want product number 5\

Path function in fast api is used for better readability
---------------------------------------
http status codes:HTTP status code basically tells the client what happened to the request.

200 → OK
201 → Created
204 → No Content

400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
405 → Method Not Allowed
409 → Conflict
422 → Unprocessable Content

500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout

HTTP Exception - used to return custom http exception if somethings happen with your api
---------------------------------------
post req
