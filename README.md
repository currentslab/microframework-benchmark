# microframework-benchmark-python
Cause who don't like fast backend

This benchmark mainly focused in stability on one process stability. 

Microframeworks benchmarked in this repo: [Bottle 0.12 ](https://bottlepy.org/), [Flask 1.0.2 ](http://flask.pocoo.org/), [Japronto 0.1.2 ](https://github.com/squeaky-pl/japronto), [Pyramid 1.10.2 ](https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html), [Sanic 18.12.0 ](https://github.com/huge-success/sanic), [Tornado 6.0.1](https://www.tornadoweb.org/en/stable/)

For simplicity, [Locust](https://locust.io/) is used to load test all framework. The Locust client is executed from either a Linode nanode or a highspeed, low latency access point. 

## Benchmark method:

All framework are under Linode 1vCPU 1GB with no additional pipeline layer. Adding any pipeline will change the final results.

1. Json serialization and delivering : Since Sanic use ujson by default, ujson is used in all framework for serialization. Hence, the result should be correlate to text delivering result as well.

2. Text delivering : Hello World

Locust will load test all frameworks for full 2 minutes, under 1000 users with a hatch rate of 100 per second. I will increase the concurrent users number untill the framework start having failed connection.

## Results

### Text

| Framework  | Total Request  | Request Per Second  | Median Response Time (ms) |
|------------|:--------------:|:-------------------:|:---------------------:|
|   Bottle   |  31976         |  269.52 | 140 |
|   Flask    |  31858 |  266.2 |  180 |
|   Japronto |  11925 |  99.59 | **61**  |
|   Pyramid  |  31981 |  268.25 | 170 |
|   Sanic*    |  11741 | 98.34  |  120 |
|   Tornado  |  11857 | 99.59  |  62 |

*Sanic : 29 failed requests

### Json

| Framework  | Total Request  | Request Per Second  | Median Response Time (ms) | Failed Requests |
|------------|:--------------:|:-------------------:|:---------------------:|:---:|
|   Bottle   |  32017         |  269.52 | 140 | 3 |
|   Flask    |  20142 |  294.99 |  270 | 0 |
|   Japronto |  11850 |  99.66 | **61**  | 0 |
|   Pyramid  |  31766 |  266.91 | 150 | 0 |
|   Sanic    |  8520 | 99.75  |  120 | 7 |
|   Tornado  |  11665 | 98.11  |  62 | 204 |

For the lowest median response time, Japronto and Tornado are the best among all 5 frameworks.

Flask, Bottle in my opinion are the best synchronous framework among all. While 

Tornado and Japronto have the better performance in async function. Do note that tornado support async function in callback form, while Jaronto use uvloop for async task. 

Note : The one million requests per second from Japronto is archieve using pipelining. However, in a real world use case, each client will only send one request per second.

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
Change the framework name to any of the available package under microframeworks : bottle, flask, japronto, pyramid, sanic, tornado

### Locust Setup

Change the filename_to_save to the current framework you are running in the linode instance.

On the project root execute this script to start text benchmark
```
locust -f benchmark/text_locust.py --no-web -c 3000 -r 100 --csv=[filename_to_save] -t2m
```

On the project root execute this script to start json benchmark
```
locust -f benchmark/text_locust.py --no-web -c 3000 -r 100 --csv=[filename_to_save] -t2m
```


# Todo
1. Run multiple times for each benchmark and use the average value
2. Include aiohttp for benchmark 
3. Auto extract benchmark result and generate the final table