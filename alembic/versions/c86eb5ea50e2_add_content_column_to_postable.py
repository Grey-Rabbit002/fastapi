"""add content column to postable

Revision ID: c86eb5ea50e2
Revises: f22c823971d1
Create Date: 2023-04-20 12:10:56.843557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c86eb5ea50e2'
down_revision = 'f22c823971d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('postable', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('postable','content')
