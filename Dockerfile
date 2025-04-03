# Dockerfile

FROM python:3.11-slim

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# expose the port uvicorn will run on
EXPOSE 8080

# run the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
