FROM apache/airflow:2.8.2-python3.10
ADD . .
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt