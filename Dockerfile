from semibit/face-match:latest

USER user
WORKDIR /app

EXPOSE 7860
CMD ["python", "app.py"]