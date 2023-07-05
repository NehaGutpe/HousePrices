import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

#create app
app =FastAPI()

#configure cors to access API from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#load the model 
rgModel=pickle.load(open("reg.pkl","rb"))


#index route, open automatically on http://127.0.0.1:80
@app.get('/')
def index():
   return {'message':'Hello, World'}

f
#using Get method
@app.get("/PredictPrice")
def getPredictPrice(total_sqft:int, bath:int, balcony:int, bhk:int ):
   # rgModel=pickle.load(open("reg.pkl","rb"))
    
    prediction=rgModel.predict([[total_sqft, bath, balcony, bhk]])
    return {
        'price': prediction[0]
    }

# run app
if __name__=="__main__":
    uvicorn.run(app, port=80, host='0.0.0.0')

# uvicorn app:app --host 0.0.0.0 --port 80
#http://127.0.0.1/PredictPrice?total_sqft=1200&bath=2&balcony=1&bhk=2