FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN ["chmod", "+x", "./entrypoint.sh"]

CMD ["gunicorn"  , "-c", "gconfig.py", "gsm.wsgi:application"]

#EXPOSE 8080
#ENTRYPOINT ["sh", "./entrypoint.sh"]