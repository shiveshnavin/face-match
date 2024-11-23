FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN apt install cmake
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 7860
CMD ["python", "app.py"]
