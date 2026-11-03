"""add password column

Revision ID: 9c97cdedffad
Revises: c2971722c470
Create Date: 2026-11-03 14:54:55.095791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c97cdedffad'
down_revision: Union[str, Sequence[str], None] = 'c2971722c470'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('password', sa.String(length=100), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'password')
