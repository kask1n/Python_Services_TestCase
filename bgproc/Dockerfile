FROM python:3.10

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

RUN mkdir bgproc && mkdir webapi

COPY ./bgproc/* ./bgproc
COPY ./webapi/main.py ./webapi

CMD ["python3", "bgproc/main.py", "--reload"]
