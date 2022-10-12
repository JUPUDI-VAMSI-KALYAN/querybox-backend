FROM python:3.10

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt 
RUN pip install -r /code/requirements.txt
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
COPY . /code


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]