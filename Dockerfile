FROM balenalib/armv7hf-debian:stretch-run

RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  apt-transport-https \
  g++ \
  python3-dev

RUN apt-get update && apt-get install -y --no-install-recommends python3-pip python3-setuptools\
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
COPY pip_packages.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN mkdir app && mkdir app/src

COPY . app/

WORKDIR app/src

CMD ["python3", "./bme280_influx.py"]
