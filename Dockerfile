from semibit/face-match:tagname

USER user
WORKDIR /app

EXPOSE 7860
CMD ["python", "app.py"]