Feature: Working with files in Dropbox
    Scenario Outline: Upload some file
        Given I have some "<file>" to upload to a "<directory>"
        When I send a POST request for upload to Dropbox "<endpoint>"
        Then the file is uploaded and the response is "200 OK"
        Examples:
            | file                | directory                            | endpoint                                      |
            | Museum-art-deco.png | /WebAPI_HomeTask/Museum-art-deco.png | https://content.dropboxapi.com/2/files/upload |

    Scenario Outline: Get metadata of some file
        Given I want to see "<file>" metadata
        When I send a POST request for file metadata to Dropbox "<endpoint>"
        Then the metadata is shown and the response is "200 OK"
        Examples:
            | file                                 | endpoint                                               |
            | /WebAPI_HomeTask/Museum-art-deco.png | https://api.dropboxapi.com/2/sharing/get_file_metadata |

    Scenario Outline: Delete some file
        Given I want to delete some "<file>"
        When I send a POST request for delete to Dropbox "<endpoint>"
        Then the file is deleted and the response is "200 OK"
        Examples:
            | file                                 | endpoint                                     |
            | /WebAPI_HomeTask/Museum-art-deco.png | https://api.dropboxapi.com/2/files/delete_v2 |