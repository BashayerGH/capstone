"""Initial migration

Revision ID: 4ea9170604b9
Revises: 
Create Date: 2022-10-04 06:44:18.583726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ea9170604b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('category', 'books', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('category', 'books', 'categories', ['category'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    # ### end Alembic commands ###
