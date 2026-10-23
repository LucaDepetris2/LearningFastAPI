
from collections.abc import Callable
from typing import Any

# Import Any: allows any type of data.
# Import Callable: represents an expected function, indicating the input and the return type.


routes: dict[str, Callable[[], Any]] = {}
# Routes: empty dictionary
# Routes[str]: the keys would be strings
# All together: Routes is a dictionary which has string keys, that are functions that receive Any data and return Any data
# Dict: the annotation that describes the type of the dictionary
# {}: is the real dictionary

def route(path: str):
    def register_path(func):
        routes[path] = func
        return func
    return register_path

# The function route receives a path (string) and register_path receives a function. This function adds to the dictionary the key path with the value of the func and returns it. Then it returns the func that receives.

@route("/shipment")
def get_shipment():
    return {
        "content": "wooden table",
        "status": "in transit"
    }

# Here I decorate my get_shipment, registering the path: shipment, and return the shipment

request: str = ""

while request != "quit":
    request = input(">   ")

    if request in routes:
        response = routes[request]()
        print(response, end="\n\n")
    else:
        print("Not found")

# Here I simulate a server with a while loop evaluating the request value. If the request (endpoint) is in my dictionary of routes, the response should be the function of the value of key path. Then I print it.