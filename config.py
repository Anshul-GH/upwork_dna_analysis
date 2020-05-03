# configuration file to hold params that can be modified

config = {
    "MIN_K": 4,
    "MAX_K": 9,
}

# method to expose the configuration variables
def get_config(param, default=None):
    cv = config.get(param)
    return cv 