FROM python:3.7-slim
RUN pip install flask
RUN pip install requests
RUN pip install pymysql
RUN pip install SQLAlchemy==1.4.17
CMD ["python","aluno.py"]