# Use the Jenkins base image
FROM jenkins/jenkins:latest

# Ignore APT warnings about not having a TTY
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root to install sudo since it doesn't exist in base image
USER root

# Update APT and install Python, UnixODBC, and other necessary items
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-pyodbc \
        python3-pytest \
        gcc \
        g++ \
        unixodbc \
        unixodbc-dev \
        curl \
        apt-transport-https
    
# Install SQL Server ODBC Driver 17 for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install msodbcsql17

# Switch back to Jenkins user
USER jenkins

# Set the working directory
WORKDIR /var/jenkins_home

# Expose Jenkins port
EXPOSE 8080