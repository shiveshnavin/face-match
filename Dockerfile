FROM python:3.10-slim

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app
RUN sudo apt install cmake

COPY --chown=user ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY --chown=user . /app

EXPOSE 7860
CMD ["python", "app.py"]
