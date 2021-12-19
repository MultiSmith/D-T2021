import pytest
from features.steps.WorkingWithFilesInDropbox import Upload, GetFileMetadata, Delete

def test_upload():
    assert 0 == Upload().test()

def test_get_file_metadata():
    assert 0  == GetFileMetadata().test()

def test_delete():
    assert 0 == Delete().test()