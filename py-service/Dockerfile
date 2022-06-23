FROM python:3.9-slim-buster

WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./
RUN pip3 install -r requirements.txt

# Bundle app source
COPY src .

EXPOSE 8080

#CMD [ "python3", "main.py"]

ENV FLASK_APP=main
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]