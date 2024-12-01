from semibit/face-match:latest

WORKDIR /app
COPY ./src/app.py /app
RUN mkdir /app/flagged
EXPOSE 7860
CMD ["python", "app.py"]