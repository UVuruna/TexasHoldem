class Decorator:
    def countExecutionMethod(method):
        def wrapper(*args, **kwargs):
            wrapper.counter += 1
            print(f"{method}Ponavlja se {wrapper.counter}. put")
            return method(*args, **kwargs)
        wrapper.counter = 0
        return wrapper

    def ListAppend(ListX):
        def decorator(method):
            def wrapper(*args, **kwargs):
                result = method(*args, **kwargs)
                ListX.extend(result)
                return result
            return wrapper
        return decorator