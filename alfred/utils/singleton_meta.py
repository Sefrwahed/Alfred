class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            i = super().__call__(*args, **kwargs)
            cls._instances[cls] = i

        return cls._instances[cls]
