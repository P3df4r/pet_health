FROM mongo:latest
RUN mkdir /home/PH
COPY pet.py /home/PH/.
COPY vet.py /home/PH/.
COPY routes.py /home/PH/.
COPY requirements.txt .
COPY index.html /home/PH/.

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install vim -y
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "/home/PH/routes.py"]
CMD ["mongod"]
