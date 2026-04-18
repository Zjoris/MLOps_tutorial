from  fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import uvicorn

app = FastAPI()

model_pipe = joblib.load('model.pkl')

@app.post("/predict")
def predict(data : dict) :
    try :
        df = pd.DataFrame([data])
        pred = model_pipe.predict(df)
        return {"prediction" : pred.tolist()[0]}
    except Exception as e :
        raise HTTPException(status_code=500, detail = str(e))
    
if __name__ == "__main__" :
    # Run API
    print("Running app")
    uvicorn.run("api:app", host = "0.0.0.0", port = 8000)