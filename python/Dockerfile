# Defines the application's image content via build commands
# that configure the image.

# Start with the python3 base image
FROM python:3

# Foces stdin, stdout, stderr to be totally unbuffered.
# Also puts then into binary mode
ENV PYTHONUNBUFFERED 1

# create a directory the code will run in
RUN mkdir /code

# change the directory that all commands will execute in
WORKDIR /code

# copy the file from this directory to /code
ADD requirements.txt /code

# run pip in the WORKDIR (that we defined above)
RUN pip install -r requirements.txt

# Copy everything in this directory to /code/
# This is after requirements due to not having to update requirements
# when a file changes.
ADD . /code/
