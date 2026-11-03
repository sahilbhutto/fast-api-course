"""create  users table

Revision ID: c2971722c470
Revises:
Create Date: 2026-11-03 14:52:22.485392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2971722c470'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("email", sa.String(50), nullable=False, unique=True, index=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
