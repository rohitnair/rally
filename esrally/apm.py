# apm_available = True
#
# try:
#     import elasticapm
# except ImportError:
#     apm_available = False
#
#
# class trace(object):
#     def __init__(self, args, **kwargs):
#         # TODO: Create a different delegate if APM API is not available
#         self.delegate = elasticapm.trace(args, **kwargs)
#
#     def __call__(self, func):
#         # TODO: Probably we need to be a bit smarter here
#         return self.delegate.__call__(func)
#
#     def __enter__(self):
#         self.delegate.__enter__()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.delegate.__exit__(exc_type, exc_val, exc_tb)
#
