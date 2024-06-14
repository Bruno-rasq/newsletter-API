import uvicorn
from fastapi import FastAPI
from newsletter.db.db_services import criar_db
from newsletter.controllers.routers import router


app = FastAPI()
app.include_router(router)
criar_db()


if __name__ == '__main__':
  uvicorn.run(app, host="0.0.0.0", port=8080)