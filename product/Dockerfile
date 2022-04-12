FROM python:3.8
COPY requirements.txt /bookapp/requirements.txt
WORKDIR /bookapp
RUN pip3 install -r requirements.txt
RUN pip3 install newrelic
copy . /bookapp
RUN chmod 777 ./startup.sh
ENTRYPOINT ["newrelic-admin", "run-program"]
#ENTRYPOINT ["python"]
ENV NEW_RELIC_LICENSE_KEY=87433a1f39f971c49a073d49ede9cc08FFFFNRAL \
    NEW_RELIC_LOG=/record.log \
    NEW_RELIC_LOG_LEVEL=info \    
    NEW_RELIC_APP_NAME="book_service" \
    NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
CMD ["./startup.sh"]
