from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return HTMLResponse(content='''
        <html>
        <body>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

@app.post("/greet")
async def greet(username: str = Form(...)):
    return f"Hello {username}, Welcome to this app for a Deployment demonstration on Render."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
