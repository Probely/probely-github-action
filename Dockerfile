FROM python:3.12-slim-bookworm

RUN pip install requests
COPY scan.py /scan.py

ENTRYPOINT ["python", "/scan.py"]
