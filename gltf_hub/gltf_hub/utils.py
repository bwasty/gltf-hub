import os

def env_var(name, default=None):
    value = os.getenv(name, default)

    if value is None:
        raise KeyError(f'Environment variable {name} is required.')

    return value
