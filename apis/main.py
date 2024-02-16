from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {
        "message": "Hello"
        }


@app.get("/credit_score")
def credit_score(age: int,working: bool, income: float):
    #prob_default = model.predict_proba([[age,working,income]])[0][0]
    prob_default = 0.5
    return {
        "prob_default": prob_default
        }


@app.post("/post_your_profile")
def post_your_profile(name: str, user:str):
    return {
        "name": name,
        "user": user
        }


#localhost:4444/credit_score?age=30&working=true&income=100000
# uvicorn main:app --reload --port 4444
#ls and cd
