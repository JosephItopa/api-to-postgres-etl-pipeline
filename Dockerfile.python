FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./export_var.sh /app/export_var.sh
COPY ./run_etl_pipeline.py /app/run_etl_pipeline.py

COPY ./extract.py /app/extract.py

COPY ./transform.py /app/trasnform.py

COPY ./load.py /app/load.py

# Run the app whenever container launches
CMD ["python3", "run_etl_pipeline.py"]