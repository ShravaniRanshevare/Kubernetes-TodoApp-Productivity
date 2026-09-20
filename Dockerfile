FROM python:3.11-slim
WORKDIR /app
COPY TodoApp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY TodoApp/ ./TodoApp
CMD ["uvicorn","TodoApp.main:app","--host","0.0.0.0","--port","8000"]