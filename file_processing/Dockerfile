FROM python:3.7.2-alpine3.9
COPY . /app
WORKDIR /app
RUN pip install -r process_file_requirements.txt
CMD python ./process_file.py