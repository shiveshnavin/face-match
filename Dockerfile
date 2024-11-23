FROM python:3.9

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"
RUN apt-get update && apt-get install -y cmake
WORKDIR /app

COPY --chown=user ./requirements.txt /app/requirements.txt
RUN pip install face_recognition gradio
COPY --chown=user . /app

EXPOSE 7860
CMD ["python", "app.py"]
