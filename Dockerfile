FROM python:3.14-alpine
LABEL org.opencontainers.image.title="bbb_exporter"
LABEL org.opencontainers.image.description="Prometheus exporter BigBlueButton services"

COPY ./bbb-exporter /app
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
EXPOSE 9688
USER nobody
ENTRYPOINT ["python"]
CMD ["server.py"]