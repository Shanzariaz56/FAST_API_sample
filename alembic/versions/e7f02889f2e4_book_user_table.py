"""book-user-table

Revision ID: e7f02889f2e4
Revises: abd1dcbf5c88
Create Date: 2024-10-02 18:51:56.400734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7f02889f2e4'
down_revision: Union[str, None] = 'abd1dcbf5c88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
