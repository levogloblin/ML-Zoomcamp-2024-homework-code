FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv
 
WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
COPY ["model2.bin", "dv.bin", "./"]
 
RUN pipenv install --system --deploy
 
COPY ["predict.py", "./"]
 
EXPOSE 9696
 
ENTRYPOINT ["waitress-serve", "--listen", "0.0.0.0:9696", "predict:app"]
