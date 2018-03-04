"""update

Revision ID: bf3dbd7af7ee
Revises: 53a75eb8f0ea
Create Date: 2018-03-04 17:08:31.721991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf3dbd7af7ee'
down_revision = '53a75eb8f0ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_test_column'), 'users', ['test_column'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_test_column'), table_name='users')
    # ### end Alembic commands ###