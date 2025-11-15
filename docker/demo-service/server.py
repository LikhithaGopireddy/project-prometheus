from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('demo_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
ERROR_COUNT = Counter('demo_errors_total', 'Total errors')
REQUEST_LATENCY = Histogram('demo_request_latency_seconds', 'Request latency')

@app.route('/')
def index():
    REQUEST_COUNT.labels(request.method, '/').inc()
    with REQUEST_LATENCY.time():
        return "Hello, World!"

@app.route('/fail')
def fail():
    REQUEST_COUNT.labels(request.method, '/fail').inc()
    with REQUEST_LATENCY.time():
        ERROR_COUNT.inc()
        return "Error!", 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
