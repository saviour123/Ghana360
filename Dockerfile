# Use the latest python image from dockerhub
FROM python:latest

# Install the web framework mojolicious
RUN pip Install -r requirements.txt 

# add your application code and set the working directory
ADD . /app
WORKDIR /app

# change the permissions and run the application
RUN chmod +x app.py
CMD ["python", "app.py"]