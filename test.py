from fastapi import FastAPI
import uvicorn

api = FastAPI()

@api.get('/random_number')
def random_no():
    import random
    val_random_number = random.randint(1, 10)

    return val_random_number

if __name__ == '__main__':
    uvicorn.run(api, host="0.0.0.0", port=8000)
