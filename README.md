# microframework-benchmark-python
Cause who don't like fast backend

This benchmark mainly focused in stability on one process stability. 

Microframeworks benchmarked in this repo: [Bottle 0.12 ](https://bottlepy.org/), [Flask 1.0.2 ](http://flask.pocoo.org/), [Japronto 0.1.2 ](https://github.com/squeaky-pl/japronto), [Pyramid 1.10.2 ](https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html), [Sanic 18.12.0 ](https://github.com/huge-success/sanic), [Tornado 6.0.1](https://www.tornadoweb.org/en/stable/)

For simplicity, [Locust](https://locust.io/) is used to load test all framework. The Locust client is executed from either a Linode nanode or a highspeed, low latency access point. 

## Benchmark method:

All framework are under Linode 1vCPU 1GB with no additional pipeline layer. Adding any pipeline will change the final results.

1. Json serialization and delivering : Since Sanic use ujson by default, ujson is used in all framework for serialization. Hence, the result should correlate to text delivering result as well.

2. Text delivering : Hello World

Locust will load test all frameworks for full 2 minutes. I will increase the concurrent users number untill the framework start having failed connection. To prevent os resource cap, resource limitation was set to 999999.

## Results

### Local server and client : Macbook Pro 2016 ( i5-7360U, 8G RAM )

Locust load test for 1 minute, total user 4,000 with hatch rate of 500 (user growth at 500 users per step)

CPU fan run at full speed, to prevent thermal throttle

#### Text ( 12 Bytes)

| Framework  | Total Request  | Median Response Time (ms) | Request Per Second  | Failed Requests |
|------------|:--------------:|:-------------------:|:---------------------:|:---:|
|   aiohttp   |  23316     |  15 | 388.58 | 0 |
|   Bottle   |  18023         | 163  | 304.52 | 163 |
|   Flask    |  19023 | 77 |  318.03 | 0 |
|   Japronto |  23868 |  7 | 399.93  | 0 |
|   Pyramid  |  20067 |  69 | 340.12 | 135 |
|   Sanic    |  16473 | 110  |  275.26 | 4 |
|   Starlette    |  17278 | 130  |  288.89 | 0 |
|   Tornado  |  23644 | 10  |  395.91 | 0 |

#### Json ( 106 Bytes )

| Framework  | Total Request  | Median Response Time (ms) | Request Per Second | Failed Requests |
|------------|:--------------:|:-------------------:|:---------------------:|:---:|
|   aiohttp   |  23459     |  11 | 392.48 | 0 |
|   Bottle   |  20778    |  74 | 350.93 | 163 |
|   Flask    |  19809 | 82  |  333.80 | 0 |
|   Japronto |  24058 |  7 | 406.88  | 0 |
|   Pyramid  |  20912 |  74 | 350.75 | 233 |
|   Sanic    |  16877 | 120  |  285.45 | 2 |
|   Starlette    |  17216 | 120   |  290.92 | 1 |
|   Tornado  |  23993 |  8 | 406.02 | 0 |

### Remote Server : Linode nanode ( North-East region )

Locust load test for 1 minute, total user 10,000 with hatch rate of 100 (user growth at 100 users per step)

#### Text

| Framework  | Total Request  | Request Per Second  | Median Response Time (ms) | Failed Requests |
|------------|:--------------:|:-------------------:|:---------------------:|:---:|
|   aiohttp   |  18908     |  313.74 | 63 | 0 |
|   Bottle   |  13250    |  221.04 | 120 | 0 |
|   Flask    |  16012 | 265.72  |  120 | 0 |
|   Japronto |  18804 |  313.17 | 62  | 0 |
|   Pyramid  |  12290 |  206.84 | 120 | 345 |
|   Sanic    |  18537 | 310.92  |  120 | 43 |
|   Starlette    |  18671 | 311.90   |  120 | 2 |
|   Tornado  |  18771 |  314.84 | 63 | 0 |
|   Django+Gunicorn  |  18052 |  730 | 152 | 0 |

#### Json

| Framework  | Total Request  | Request Per Second  | Median Response Time (ms) | Failed Requests |
|------------|:--------------:|:-------------------:|:---------------------:|:---:|
|   aiohttp   |  18924     |  317.42 | 63 | 0 |
|   Bottle   |  13402    |  225.04 | 120 | 0 |
|   Flask    |  13393 | 224.14  |  120 | 0 |
|   Japronto |  19003 |  319.82 | 62  | 0 |
|   Pyramid  |  13316 |  223.58 | 120 | 0 |
|   Sanic    |  18525 | 311.76  |  120 | 42 |
|   Starlette    |  17260 | 288.02   |  120 | 3 |
|   Tornado  |  18939 |  317.33 | 63 | 0 |


For the lowest median response time, Japronto and Tornado are the best among all 5 frameworks.

Flaskin my opinion are the best synchronous framework among all. aiohttp, Tornado, Japronto have the better performance in async function. Do note that tornado support async function in callback form, while Japronto use uvloop for async task. 

Note : The one million requests per second from Japronto is archieved using pipelining. However, in a real world use case, each client will only send one request per second.

## Setup

### Server Setup

All clone this repo into a linode nanonode and install local dependencies using virtualenv

```
    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
```

Start running framework
```
python -m microframeworks.[framework name].app
```

For Django 
```
cd fullframeworks/django_test
gunicorn -b 0.0.0.0:8000 django_test.wsgi --workers=1
```

Change the framework name to any of the available package under microframeworks : bottle, flask, japronto, pyramid, sanic, tornado

### Locust Setup

Change the filename_to_save to the current framework you are running in the linode instance.

On the project root execute this script to start text benchmark
```
locust -f benchmark/text_locust.py --no-web -c 3000 -r 100 -t2m --csv=[filename_to_save] 
```

On the project root execute this script to start json benchmark
```
locust -f benchmark/text_locust.py --no-web -c 3000 -r 100 -t2m --csv=[filename_to_save] 
```


# Todo

1. Run multiple times for each benchmark and use the average value
2. Include aiohttp for benchmark 
3. Auto extract benchmark result and generate the final table
4. Track memory footprint for each framework
5. File serving benchmark


## Data content value

1. Data for text, json are imported from microframeworks.settings, with Django as exception( should be fixed in the future )
