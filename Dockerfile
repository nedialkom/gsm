FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ["chmod", "+x", "./entrypoint.sh"]
EXPOSE 8080
ENTRYPOINT ["sh", "./entrypoint.sh"]