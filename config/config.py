# In template, functions are across different workflows.
import os.path

KAFKA_IP = '172.31.3.10'
GATEWAY_IP = '172.31.10.85'
COUCHDB_IP = '172.31.3.10'
WORKER_ADDRS = ['172.31.41.77', '172.31.34.103', '172.31.38.115']

COUCHDB_URL = f'http://openwhisk:openwhisk@{COUCHDB_IP}:5984/'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
# RESOURCE_MONITOR_URL = 'http://127.0.0.1:7998/{}'
KAFKA_URL = f'{KAFKA_IP}:9092'
PREFETCHER_URL = 'http://127.0.0.1:8002/{}'
GATEWAY_URL = f'{GATEWAY_IP}:7000'

FUNCTIONS_INFO_PATH = '../../benchmark'
os.environ["HOME"] = '/home/ubuntu'
WORKFLOWS_INFO_PATH = {
                       'video': os.path.expanduser('~/FaaSFlow/benchmark/video'),
                       'wordcount': os.path.expanduser('~/FaaSFlow/benchmark/wordcount'),
                       'recognizer': os.path.expanduser('~/FaaSFlow/benchmark/recognizer'),
                       'svd': os.path.expanduser('~/FaaSFlow/benchmark/svd')}
if os.path.exists('/state/partition2/FaaSFlow'):
    PREFETCH_POOL_PATH = '/state/partition2/FaaSFlow/prefetch_pool'
    FILE_CONTROLLER_PATH = '/state/partition2/FaaSFlow/file_controller'
else:
    PREFETCH_POOL_PATH = os.path.expanduser('~/FaaSFlow/prefetch_pool')
    FILE_CONTROLLER_PATH = os.path.expanduser('~/FaaSFlow/file_controller')
CHUNK_SIZE = 1 * 1024 * 1024

DOCKER_CPU_QUOTA = 100000

REDIS_EXPIRE_SECONDS = 100
# COLLECT_CONTAINER_RESOURCE = False
KAFKA_CHUNK_TEST = False
DISABLE_PRESSURE_AWARE = False
