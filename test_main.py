from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Checking the response when accessing the root
# Проверка ответа при обращении в корень
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
            "message": "Hello, It is application - translater.\n\
 To translate from English to Russian, send the tetx to translate in /en-ru/,\n\
 To translate from Russian to English, send the tetx to translate in /ru-en/"}
    
# Checking the translation function from English to Russian
# Проверка функции перевода с английского на русский

def test_en_ru_translate():
    response = client.post("/en-ru/",
                           json={"text": "World"})
    assert response.status_code == 200
    assert response.json() == "Весь мир"

# Checking the translation function from Russian to English
# Проверка функции перевода с русского на английский

def test_ru_en_translate():
    response = client.post("/ru-en/",
                           json={"text": "Весь мир"})
    assert response.status_code == 200
    assert response.json() == "World"