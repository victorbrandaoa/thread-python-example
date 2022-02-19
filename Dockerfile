FROM python:3.8

WORKDIR /src

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD python src/__main__.py
