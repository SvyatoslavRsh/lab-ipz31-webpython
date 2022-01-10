"""empty message

Revision ID: 944c02e11e5f
Revises: 26c1de74dc8e
Create Date: 2022-01-10 18:16:43.460807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '944c02e11e5f'
down_revision = '26c1de74dc8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.drop_column('departure_time')
        batch_op.drop_column('departure_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.add_column(sa.Column('departure_date', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('departure_time', sa.VARCHAR(length=50), nullable=True))

    # ### end Alembic commands ###
