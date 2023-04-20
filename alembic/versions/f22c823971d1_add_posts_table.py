"""add posts table

Revision ID: f22c823971d1
Revises: 
Create Date: 2023-04-20 11:44:40.424267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f22c823971d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('postable', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('postable')
    pass
