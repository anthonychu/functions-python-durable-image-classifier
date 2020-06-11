FROM mcr.microsoft.com/azure-functions/python:3.0.13864-python3.7-appservice


WORKDIR /home/site/wwwroot
COPY requirements.txt .
# https://github.com/MicrosoftDocs/azure-docs/issues/40134
RUN pip3 install --target=".python_packages/lib/site-packages" -r requirements.txt

COPY . .

