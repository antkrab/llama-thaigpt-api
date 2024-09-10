from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import requests

prompt = {
    "prompt":"<s>[INST] <<SYS>>\nYou are a question answering assistant. Answer the question as truthful and helpful as possible คุณคือผู้ช่วยตอบคำถาม จงตอบคำถามอย่างถูกต้องและมีประโยชน์ที่สุด <</SYS>>\n\nสวัสดี ตอนนี้กี่โมง[/INST]",
    "n_predict":256,"stop": ["</s>"]
}
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"welcome to root"}

@app.post("/test")
async def test():
    try:
        response = requests.post("http://llamacpp:8080/completion",json=prompt)
        return response.json()["content"]
    except Exception as e :
        print(e)

@app.post("/testnoex")
async def test():
    response = requests.post("http://llamacpp:8080/completion",json=prompt)
    return response.json()["content"]
