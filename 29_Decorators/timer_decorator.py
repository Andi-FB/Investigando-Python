from timeit import default_timer


def timer(method):
    def method_wrapper(self, balance):
        start = default_timer()
        method(self, balance)
        end = default_timer()
        msg = 'returned from: {0} it took: {1} seconds'.format(method.__name__, (end - start))
        print(msg)
    return method_wrapper
