import pytest
from features.steps.WorkingWithFilesInDropbox import Upload, GetFileMetadata, Delete


def test_upload():
    Upload().testing()

def test_get_file_metadata():
    GetFileMetadata().testing()

def test_delete():
    Delete().testing()