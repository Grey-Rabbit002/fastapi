"""add foreign key to postablel

Revision ID: 01dc372c4750
Revises: 733ed035403f
Create Date: 2023-04-20 12:14:18.867078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01dc372c4750'
down_revision = '733ed035403f'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.add_column('postable', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="postable", referent_table="usertable", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
