FROM python:3.8
COPY requirements.txt /frontend/requirements.txt
WORKDIR /frontend
RUN pip3 install -r requirements.txt
RUN pip3 install newrelic
COPY . /frontend
ENTRYPOINT ["newrelic-admin", "run-program"]
ENV NEW_RELIC_LICENSE_KEY=$ENTER_YOUR_KEY_HEAR \
    NEW_RELIC_APP_NAME="flask_app" \
    NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
CMD ["chmod 777 app.py"]
CMD ["python3", "app.py"]
