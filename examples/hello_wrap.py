from globus_compute_sdk import Executor
from typing import Callable, Any

# The endpoint UUID
ENDPOINT_ID = "1e4f9309-f8c0-45e4-aac6-f0cf39a87a42"

def globus_compute_executor(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for executing functions remotely using Globus Compute Executor.

    Args:
        func (Callable[..., Any]): The function to execute remotely.

    Returns:
        Callable[..., Any]: A wrapped function that submits to Globus Compute.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        with Executor(endpoint_id=ENDPOINT_ID) as gce:
            print(f"Submitting function '{func.__name__}' with args={args} kwargs={kwargs}")
            future = gce.submit(func, *args, **kwargs)
            print("Function submitted, waiting for result...")
            result = future.result()
            print(f"Function '{func.__name__}' completed with result: {result}")
            return result

    return wrapper

# Example usage
@globus_compute_executor
def say_hello(name: str) -> str:
    return f"Hello {name}!"

if __name__ == "__main__":
    # Call the decorated function
    print(say_hello("friend"))