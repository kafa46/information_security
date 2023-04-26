"""empty message

Revision ID: 062b3ea32e84
Revises: 
Create Date: 2023-04-10 10:58:00.863590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '062b3ea32e84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hacker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('writer', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hacker')
    # ### end Alembic commands ###