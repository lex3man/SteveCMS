FROM python
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN apt update \
#     && apt add postgresql-dev gcc python3-dev musl-dev
#
RUN mkdir /usr/src/app/static

RUN pip install --upgrade pip

COPY req.txt ./

RUN pip install --no-cache-dir -r req.txt

COPY ./entrypoint.sh .

RUN chmod +x ./entrypoint.sh

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
