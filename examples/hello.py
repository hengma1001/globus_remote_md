"""Globus Compute example.

Requires environment with the following dependency:
pip install globus-compute-sdk

Note: You need to use the same python version as is running on the endpoint.

Note: The first time your run the function on a new computer you will
need to authenticate with Globus.

Note: If it's been a while since you've run the function, it will take a
minute to warm up. That's because the job has to get through the queue and
import the python libraries, etc. Subsequent calls will be faster.
"""
from globus_compute_sdk import Executor

# The endpoint UUID
ENDPOINT_ID = '1e4f9309-f8c0-45e4-aac6-f0cf39a87a42'

def say_hello(name: str) -> str:
    return f"Hello {name}!"

if __name__ == '__main__':
    # Initialize the compute executor
    gce = Executor(endpoint_id=ENDPOINT_ID)

    # Submit the remote procedure call
    fut = gce.submit(say_hello, 'friend')

    print('Running function', fut)

    # Collect the return result
    result = fut.result()

    # Print the result
    print(result)