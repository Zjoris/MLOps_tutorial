FROM python:3.13.11

WORKDIR /app

COPY api.py /app/
COPY model.pkl /app/
COPY requirements.txt /app/
COPY static/ /app/static/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]