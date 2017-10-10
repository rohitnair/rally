import elasticapm


@elasticapm.trace()
def hello():
    print("Hello APM")


if __name__ == '__main__':
    client = elasticapm.Client()
    client.config.app_name = 'hello-apm'
    client._framework = 'None'
    client._framework_version = 'None'

    client.begin_transaction('hello')
    hello()
    client.end_transaction('hello')
