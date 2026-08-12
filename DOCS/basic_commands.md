1. python -m venv myenv
myenv\Scripts\activate
pip install fastapi uvicorn pydantic    
uvicorn main:app --reload
