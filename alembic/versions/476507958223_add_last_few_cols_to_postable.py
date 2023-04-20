"""add last few cols to postable

Revision ID: 476507958223
Revises: f9d9a7af6f4a
Create Date: 2023-04-20 12:17:34.532061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '476507958223'
down_revision = 'f9d9a7af6f4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('postable', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('postable', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('postable', 'published')
    op.drop_column('postable', 'created_at')
    pass
