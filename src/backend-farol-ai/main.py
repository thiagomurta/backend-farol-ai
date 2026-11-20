from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Backend farol-ai rodando com uv!"}


# def main():
#     print("Hello from backend-farol-ai!")
#
#
# if __name__ == "__main__":
#     main()
