"""add user table

Revision ID: 733ed035403f
Revises: c86eb5ea50e2
Create Date: 2023-04-20 12:12:27.535663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '733ed035403f'
down_revision = 'c86eb5ea50e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('usertable',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('paswd', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('usertable')
    pass
