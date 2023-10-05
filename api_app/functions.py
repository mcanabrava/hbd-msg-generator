import openai
import time
from functools import wraps
from flask_limiter import Limiter 

# Define your get_completion function here
def get_completion(prompt, model="gpt-3.5-turbo"):
    """
    Generate a completion using OpenAI's GPT-3 model.

    Args:
        prompt (str): The user's prompt for message generation.
        model (str, optional): The GPT-3 model to use (default is "gpt-3.5-turbo").

    Returns:
        str: The generated message.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
    )
    return response.choices[0].message["content"]

# Define a custom throttling decorator
def throttle(seconds):
    """
    Decorator to throttle requests by introducing a delay.

    Args:
        seconds (int): The delay in seconds.

    Returns:
        function: The decorator function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Introduce a delay before processing the request
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator
