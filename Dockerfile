FROM ubuntu:latest
LABEL authors="kask1n"

ENTRYPOINT ["top", "-b"]

FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python3", "-m", "uvicorn", "main:app", "--reload"]
