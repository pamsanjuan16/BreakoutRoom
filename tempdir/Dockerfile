FROM python
RUN pip install flask
RUN pip install ipapi
COPY  ./templates /home/myapp/templates/
COPY  ./static /home/myapp/static/
COPY  server.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/server.py
