FROM python:3.6

COPY * /usr/src/app/

RUN ls -l /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt

EXPOSE 5000

# RUN sh /usr/src/app/build.sh
# RUN export FLASK_APP=/usr/src/app/handler.py

# RUN flask run

CMD ["python", "/usr/src/app/handler.py"]