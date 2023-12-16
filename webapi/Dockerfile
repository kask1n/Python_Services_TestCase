FROM python:3.10

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./webapi ./

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
