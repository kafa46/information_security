"""empty message

Revision ID: ab632fbd2bde
Revises: 1b71868b5b1f
Create Date: 2023-04-06 14:26:27.591361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab632fbd2bde'
down_revision = '1b71868b5b1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=200), nullable=True))
        batch_op.drop_column('subject')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subject', sa.VARCHAR(length=200), nullable=True))
        batch_op.drop_column('title')

    # ### end Alembic commands ###
