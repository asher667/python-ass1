
import time
from functools import wraps


def rate_limit(max_calls: int, period: int):

    def decorator(func):
        calls = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls

            now = time.time()

            calls = [timestamp for timestamp in calls
                     if now - timestamp < period]

            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")

            calls.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(max_calls=3, period=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"


if __name__ == "__main__":
    print(fetch_user_data(101))
    print(fetch_user_data(102))
    print(fetch_user_data(103))


