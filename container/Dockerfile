FROM python:3

ADD tweets_pos_clean.txt /

ADD tweets_neg_clean.txt /

ADD test_naive_bayes.py /

RUN pip install nltk pandas

#ENTRYPOINT ["python","./test_naive_bayes.py"]
