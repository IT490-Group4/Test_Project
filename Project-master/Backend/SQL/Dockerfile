FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# wait_for_it.sh is a little nice than sleeping
# https://docs.docker.com/compose/startup-order/
CMD ["./wait-for-it.sh", "mysql:3306", "--", "python", "database.py"]
