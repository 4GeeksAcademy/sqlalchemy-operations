"""Merging heads

Revision ID: 9a741a25efdc
Revises: 66bdb95b95c6, 66db907c1e5f
Create Date: 2024-06-06 13:20:24.225072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a741a25efdc'
down_revision: Union[str, None] = ('66bdb95b95c6', '66db907c1e5f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
