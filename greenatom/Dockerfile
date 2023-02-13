FROM python

ENV APP_HOME=/greenatom/
RUN mkdir -p $APP_HOME


WORKDIR $APP_HOME

# install dependencies
RUN pip install --upgrade pip
COPY greenatom/requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY greenatom/. $APP_HOME


CMD ["python","main.py"]

