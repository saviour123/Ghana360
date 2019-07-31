# Use the latest python image from dockerhub
FROM python:latest

# add your application code and set the working directory
ADD . /app
WORKDIR /app

# Install the web framework mojolicious
RUN pip install -r requirements.txt 

# change the permissions and run the application
RUN chmod +x app.py
CMD ["python", "app.py"]