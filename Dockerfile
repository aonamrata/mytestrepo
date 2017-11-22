FROM python:3.6

RUN echo "Starting web.."
RUN rm -frv /usr/src/app/*
COPY * /usr/src/app/

RUN chmod 777 /usr/src/app/create_tables.sh
RUN ls -l /usr/src/app/

RUN echo "Installing requirements.."
RUN pip install -r /usr/src/app/requirements.txt

EXPOSE 5000

# RUN sh /usr/src/app/build.sh
# RUN export FLASK_APP=/usr/src/app/handler.py

# RUN flask run

# RUN echo "Creating tables.."
# CMD ["/usr/src/app/create_tables.sh"]

CMD ["python", "/usr/src/app/handler.py"]
