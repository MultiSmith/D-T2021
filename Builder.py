from abc import ABC, abstractclassmethod
import requests

class Builder(ABC):
    @abstractclassmethod
    def set_headers(self):
        pass
    
    @abstractclassmethod
    def set_body(self):
        pass

    @abstractclassmethod
    def set_request(self):
        pass

    @abstractclassmethod
    def get_response(self):
        pass

class UploadBuilder(Builder):
    def __init__(self):
        self.headers = {}
        self.body = {}

    def set_headers(self, headers_):
        self.headers = headers_

    def set_body(self, file):
        self.body = file

    def set_request(self, endpoint):
        self.response = requests.post(url = endpoint, headers = self.headers, data = self.body)

    def get_response(self):
        return self.response


class GetFileMetadataBuilder(Builder):
    def __init__(self):
        self.headers = {}
        self.body = {}    

    def set_headers(self, headers_):
        self.headers = headers_

    def set_body(self, file):
        self.body = file

    def set_request(self, endpoint):
        self.response = requests.post(url = endpoint, headers = self.headers, data = self.body)

    def get_response(self):
        return self.response

class DeleteBuilder(Builder):
    def __init__(self):
        self.headers = {}
        self.body = {}

    def set_headers(self, headers_):
        self.headers = headers_

    def set_body(self, file):
        self.body = file

    def set_request(self, endpoint):
        self.response = requests.post(url = endpoint, headers = self.headers, data = self.body)

    def get_response(self):
        return self.response