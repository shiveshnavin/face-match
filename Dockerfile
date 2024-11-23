from semibit/face-match:latest

WORKDIR /app
RUN mkdir /app/flagged
EXPOSE 7860
CMD ["python", "app.py"]