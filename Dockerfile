FROM  efreidevopschina.azurecr.io/cache/library/python:3.10-alpine

COPY . .

CMD ["python", "calc.py"]

