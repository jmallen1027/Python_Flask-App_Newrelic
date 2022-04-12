FROM python:3.8
COPY requirements.txt /frontend/requirements.txt
WORKDIR /frontend
RUN pip3 install -r requirements.txt
copy . /frontend
ENTRYPOINT ["python"]
CMD ["app.py"]
