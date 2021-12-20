from behave import *
import sys
import os
from Builder import UploadBuilder, GetFileMetadataBuilder, DeleteBuilder


class Upload():
    def __init__(self):
        self.Upload = UploadBuilder()

    @given(u'I have some "{file}" to upload to a "{directory}"')
    def set_headers_body(self, file, directory):
        self.Upload.set_headers({
                "Content-Type": "application/octet-stream",
                "Authorization": "Bearer L12J_8DNkQYAAAAAAAAAAdQov2saKF98tz3bY0wje-JCnPKa2tkAGd-v7V0SFv1N",
                "Dropbox-API-Arg": '{"path":"' + directory + '","mode": "add"}'
        })
        f = open(file, "rb")
        self.Upload.set_body(f.read())

    @when(u'I send a POST request for upload to Dropbox "{endpoint}"')
    def set_request(self, endpoint):
        self.response = self.Upload.set_request(endpoint)
    
    @then(u'the file is uploaded and the response is "200 OK"')
    def get_response(self):
        assert self.Upload.get_response().status_code == 200, print(self.Upload.get_response())

    def testing(self):
        self.set_headers_body("Museum-art-deco.png", "/WebAPI_HomeTask/Museum-art-deco.png")
        self.set_request("https://content.dropboxapi.com/2/files/upload")
        self.get_response()


class GetFileMetadata():
    def __init__(self):
        self.GetFileMetadata = GetFileMetadataBuilder()
    
    @given(u'I want to see "{file}" metadata')
    def set_headers_body(self, file):
        self.GetFileMetadata.set_headers({
                "Content-Type": "application/json",
                "Authorization": "Bearer L12J_8DNkQYAAAAAAAAAAdQov2saKF98tz3bY0wje-JCnPKa2tkAGd-v7V0SFv1N"
        })
        self.GetFileMetadata.set_body('{"file": "' + file + '", "actions": []}')

    @when(u'I send a POST request for file metadata to Dropbox "{endpoint}"')
    def set_request(self, endpoint):
        self.GetFileMetadata.set_request(endpoint)

    @then(u'the metadata is shown and the response is "200 OK"')
    def get_response(self):
        assert self.GetFileMetadata.get_response().status_code == 200, print(self.GetFileMetadata.get_response())

    def testing(self):
        self.set_headers_body("/WebAPI_HomeTask/Museum-art-deco.png")
        self.set_request("https://api.dropboxapi.com/2/sharing/get_file_metadata")
        self.get_response()


class Delete():
    def __init__(self):
        self.Delete = DeleteBuilder()
    
    @given(u'I want to delete some "{file}"')
    def set_headers_body(self, file):
        self.Delete.set_headers({
                "Content-Type": "application/json",
                "Authorization": "Bearer L12J_8DNkQYAAAAAAAAAAdQov2saKF98tz3bY0wje-JCnPKa2tkAGd-v7V0SFv1N"
        })
        self.Delete.set_body('{"path": "' + file + '"}')

    @when(u'I send a POST request for delete to Dropbox "{endpoint}"')
    def set_request(self, endpoint):
        self.Delete.set_request(endpoint)

    @then(u'the file is deleted and the response is "200 OK"')
    def get_response(self):
        assert self.Delete.get_response().status_code == 200, print(self.Delete.get_response())

    def testing(self):
        self.set_headers_body("/WebAPI_HomeTask/Museum-art-deco.png")
        self.set_request("https://api.dropboxapi.com/2/files/delete_v2")
        self.get_response()