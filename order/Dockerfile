FROM python:3.8
COPY requirements.txt /orderapp/requirements.txt
WORKDIR /orderapp
RUN pip3 install -r requirements.txt
RUN pip3 install newrelic
copy . /orderapp
RUN chmod 777 ./startup.sh
ENTRYPOINT ["newrelic-admin", "run-program"]
ENV NEW_RELIC_LICENSE_KEY=87433a1f39f971c49a073d49ede9cc08FFFFNRAL \
    NEW_RELIC_LOG=orders.log \
    NEW_RELIC_APP_NAME="order_service" \
    NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
CMD ["./startup.sh"]
