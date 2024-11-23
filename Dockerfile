FROM python:3.9

# RUN useradd -m -u 1000 user
# USER user
# ENV PATH="/home/user/.local/bin:$PATH"
RUN apt-get update && apt-get install -y cmake
WORKDIR /app
# RUN apt install cmake
# RUN pip install --no-cache-dir --upgrade cmake

COPY --chown=user ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY --chown=user . /app

EXPOSE 7860
CMD ["python", "app.py"]
