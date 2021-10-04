FROM python:3.8
WORKDIR /src
COPY . . 
COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py"]
