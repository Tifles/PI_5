from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Item(BaseModel):
    text: str

# creating a FastAPI application in the app variable
app = FastAPI()

# Uploading pre-trained models

tokenizer_en_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
model_en_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
tokenizer_ru_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model_ru_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")

# Response with instructions when accessing the root
@app.get("/")
async def root():
    """Returns the name and parameters for the translation"""
    return {
            "message": "Hello, It is application - translater.\n\
 To translate from English to Russian, send the tetx to translate in /en-ru/,\n\
 To translate from Russian to English, send the tetx to translate in /ru-en/"}

# Translation from English to Russian         
@app.post("/en-ru/")
def predict(item: Item):
    """Translate text from English to Russian"""
    orig_text = item.text
    inputs = tokenizer_ru_en(orig_text, return_tensors="pt")
    output = model_ru_en.generate(**inputs, max_new_tokens=100)
    out_text = tokenizer_ru_en.batch_decode(output, skip_special_tokens=True)
    return  out_text[0]

# Translation from Russian to English
@app.post("/ru-en/")
def predict(item: Item):
    """Translate text from Russian to English"""
    orig_text = item.text
    inputs = tokenizer_en_ru(orig_text, return_tensors="pt")
    output = model_en_ru.generate(**inputs, max_new_tokens=100)
    out_text = tokenizer_en_ru.batch_decode(output, skip_special_tokens=True)
    return  out_text[0]