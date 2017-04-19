FROM python:3
COPY tweets_pos_clean.txt /tmp/
COPY tweets_neg_clean.txt /tmp/
COPY test_naive_bayes.py /tmp/
RUN pip install nltk pandas
ENTRYPOINT cd /tmp && python test_naive_bayes.py




