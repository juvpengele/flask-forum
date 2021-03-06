"""empty message

Revision ID: fb18e1093bb6
Revises: 5bfd3260a3a6
Create Date: 2020-10-26 08:39:09.072612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb18e1093bb6'
down_revision = '5bfd3260a3a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('threads', sa.Column('comments_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('threads', 'comments_count')
    # ### end Alembic commands ###
