# PI_5
Practical assignment for the fifth module of the discipline "Software Engineering" UrFU.   
Russian Russian text translation application for English to English and Russian to English.    
It is intended to help you work with texts in a foreign language (Reading documentation, preparing letters...)

## TranslaterML(API)

### Launching the application

To run the application, you need to install the dependencies and run the uvicorn:
 - Installing dependencies
```bash
pip install -r requirements.txt
```
 - run the application (Linux)
```bash
uvicorn  app:app
```
- run the application (Windows)
```bash
python -m uvicorn  app:app
```
- run the test
```bash
pytest test_main.py
```

#### The following ready-made models were used:
Helsinki-NLP/opus-mt-en-ru     
Helsinki-NLP/Opus-mt-ru-en

@InProceedings{TiedemannThottingal:EAMT2020,
  author = {J{\"o}rg Tiedemann and Santhosh Thottingal},
  title = {{OPUS-MT} — {B}uilding open translation services for the {W}orld},
  booktitle = {Proceedings of the 22nd Annual Conferenec of the European Association for Machine Translation (EAMT)},
  year = {2020},
  address = {Lisbon, Portugal}

# PI_5
Практическое задание по пятому модулю дисциплины "Программная инженерия" УрФУ.   
Приложение для перевода текста с английского на русский и русского на английский.   
Предназначено для помощи в  работе с текстами на иностранном языке (Чтение документации, подготовка писем...)   

### Запуск приложения

Чтобы запустить приложение, вам необходимо установить зависимости и запустить uvicorn:

 - Установка зависимостей
```bash
pip install -r requirements.txt
```
 - Запуск приложения (Linux)
```bash
uvicorn  app:app
```
 - Запуск приложения (Windows)
```bash
python -m uvicorn  app:app
```
- Запуск тестирования
```bash
pytest test_main.py
```

### Были использованы следующие готовые модели:
Helsinki-NLP/opus-mt-en-ru    
Helsinki-NLP/Opus-mt-ru-en
