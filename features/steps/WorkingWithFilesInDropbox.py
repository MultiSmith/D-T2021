from behave import *
import requests

#UPLOAD

@given(u'I have some "{file}" to upload to a "{directory}"')
def step_impl(context, file, directory):
    f = open(file, "rb")
    context.png = f.read()
    context.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer dSS6on6CQ_AAAAAAAAAAAXDWQTN5tv_RtTqGazhbFS8KSt09Xmh27Y-InA0Q7LlW",
            "Dropbox-API-Arg": '{"path":"' + directory + '","mode": "add"}'
    }

@when(u'I send a POST request for upload to Dropbox "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.post(url = endpoint, headers = context.headers, data = context.png)

@then(u'the file is uploaded and the response is "200 OK"')
def step_impl(context):
    assert context.response.status_code == 200, print(context.response)


#GET FILE METADATA

@given(u'I want to see "{file}" metadata')
def step_impl(context, file):
    context.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer dSS6on6CQ_AAAAAAAAAAAXDWQTN5tv_RtTqGazhbFS8KSt09Xmh27Y-InA0Q7LlW"
    }
    context.body = '{"file": "' + file + '", "actions": []}'

@when(u'I send a POST request for file metadata to Dropbox "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.post(url = endpoint, headers = context.headers, data = context.body)

@then(u'the metadata is shown and the response is "200 OK"')
def step_impl(context):
    assert context.response.status_code == 200, print(context.response)


# DELETE

@given(u'I want to delete some "{file}"')
def step_impl(context, file):
    context.headers = {
            "Content-Type": "application/octet-stream",
            "Authorization": "Bearer dSS6on6CQ_AAAAAAAAAAAXDWQTN5tv_RtTqGazhbFS8KSt09Xmh27Y-InA0Q7LlW"
    }
    context.body = '{"path": "' + file + '"}'

@when(u'I send a POST request for delete to Dropbox "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.post(url = endpoint, headers = context.headers, data = context.body)

@then(u'the file is deleted and the response is "200 OK"')
def step_impl(context):
    assert context.response.status_code == 200, print(context.response)