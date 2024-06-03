from models import db, People
from db_operations import Database_Operations
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy import select


@pytest.fixture
def session():
    session=UnifiedAlchemyMagicMock()
    yield session


def test_people_create(session):
  ops=Database_Operations(session=session)
  output=ops.people_create(name="Testing people")
  assert output is not None
     