import uvicorn
from fastapi import FastAPI
from database import Base, engine
from controllers import resume_controller

app = FastAPI()

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inclui os roteadores dos controladores
app.include_router(resume_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)