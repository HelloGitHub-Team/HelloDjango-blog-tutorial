from haystack.backends.elasticsearch2_backend import Elasticsearch2SearchBackend, Elasticsearch2SearchEngine

DEFAULT_FIELD_MAPPING = {'type': 'string', "analyzer": "ik_max_word", "search_analyzer": "ik_smart"}


class Elasticsearch2IkSearchBackend(Elasticsearch2SearchBackend):

    def __init__(self, *args, **kwargs):
        self.DEFAULT_SETTINGS['settings']['analysis']['analyzer']['ik_analyzer'] = {
            "type": "custom",
            "tokenizer": "ik_max_word",
        }
        super(Elasticsearch2IkSearchBackend, self).__init__(*args, **kwargs)


class Elasticsearch2IkSearchEngine(Elasticsearch2SearchEngine):
    backend = Elasticsearch2IkSearchBackend
