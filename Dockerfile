from semibit/face-match:latest

USER user
WORKDIR /app
RUN mkdir /usr/src/app/flagged
RUN mkdir /app/flagged
EXPOSE 7860
CMD ["python", "app.py"]