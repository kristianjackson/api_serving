from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix='/student')

@app.get("/", tags=["Root"])
async def read_root():
    return{"message": "Welcome to this fantastic app!"}

@app.post('/diamond', tags=["Diamond Prices"])
def predict_diamond(caret_weight, cut, color, clarity, polish, symmetry, report):
    data = pd.Dataframe([[caret_weight, cut, color, clarity, polish, symmetry, report]])
    data.columns = ['Caret Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report']
    
    model = load_model('diamond_pipeline')
    
    predictions = predict_model(model, data)
    return {'prediction': int(predictions['Label'][0])}
