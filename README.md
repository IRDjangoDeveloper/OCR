# OCR
Optical character recognition with django framwork

install project

step 1 :
install tessract-ocr package on your Linux:
sudo apt-get install tesseract-ocr

step 2: create virtual envirement for project:
python3 -m venv venv

step 3: install requirements package:
pip install -r requirements.txt

step 4: active venv:
source mypython/bin/activate

step 5: migrate models:
python manage.py makemigrations
python manage.py migrate

last step: run project:
python manage.py runserver

enjoy:))
