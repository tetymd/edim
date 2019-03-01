FROM python:3.6

RUN apt install git && \
    pip install pipenv

RUN git clone https://github.com/tetymd/edim.git && \
    cd edim && \
    pipenv install

CMD pipenv run python edim.py
