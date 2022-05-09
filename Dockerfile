FROM public.ecr.aws/lambda/python:3.9

RUN mkdir /gmail-puller
WORKDIR /gmail-puller

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--allow-root"]
