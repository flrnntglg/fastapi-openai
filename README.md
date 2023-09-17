# fastapi-openai

This is a FastAPI-based web application that provides travel recommendations for the Philippines based on the season. It uses the OpenAI GPT-3.5 Turbo model to generate recommendations.

# Prerequisites
Before running the application, make sure you have the following:

* python 3.7+
* fastapi
* uvicorn
* openai
* decouple

# Set up
1. Clone this repository
2. Change to the project directory
```
cd fastapi-openai
```
3. Create a virtual environment
```
python -m venv venv
``` 
4. Activate virtual environment
```
# Linux
 .venv/bin/activate
```
```
# Windows
venv\Scripts\activate
```  
5. Install the requirments
```
pip install -r requirements.txt
```
# Configuration
Before running the application, you need to set your OpenAI API key in a .env file. 
```
OPENAI_API_KEY=your-openai-api-key
```
Replace your-openai-api-key with your actual OpenAI API key.

# Run the Application
To start the application, use the following command:
```
uvicorn main:app --host localhost --port 3000 --reload
```
This will run the application locally on http://localhost:3000/.

# Usage
* Access the web application by opening your web browser and navigating to http://localhost:3000/ or http://localhost:3000/docs
* Select a country (currently, only "Philippines" is supported) and a season (e.g., "Summer" or "Rainy") to get travel recommendations.
* Click the "Recommendations" button, and the application will display recommendations.
