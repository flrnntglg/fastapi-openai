import openai
import uvicorn
from decouple import config
from fastapi import FastAPI, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse


openai.api_key = config("OPENAI_API_KEY")

app = FastAPI()

# Serve static files (HTML, CSS, and JavaScript)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 for HTML rendering 
templates = Jinja2Templates(directory="static")

# travel recommendations for the Philippines
travel_recommendations = {
    "Philippines": {
        "Summer": [
            "Enjoy island hopping in Boracay.",
            "Go diving in Apo Reef Natural Park.",
            "Experience the Pahiyas Festival in Lucban."
        ],
        "Rainy": [
            "Visit museums and galleries in Manila.",
            "Enjoy hot coffee in Baguio City.",
            "Enjoy the hot springs in Pansol Laguna "
        ]
    },
}

# FastAPI routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/recommendations/")
async def get_recommendations(
    country: str = Query(..., description="One country - Philippines"),
    season: str = Query(..., description="The season in which recommendations are desired (e.g., 'Summer', 'Rainy').")
):

    recommendations = travel_recommendations.get(country, {}).get(season, [])

    try:
        generated_recommendations = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Recommend travel activities in {country} during {season} season.",
            max_tokens=100,  
        ).choices[0].text
    except Exception as e:
        generated_recommendations = f"Error: {e}"
       

    return {
        "Country": country,
        "Season": season,
        "Recommendations": recommendations,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)

