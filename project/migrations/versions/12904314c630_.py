"""empty message

Revision ID: 12904314c630
Revises: 9279fd146950
Create Date: 2021-12-04 18:07:59.319610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12904314c630'
down_revision = '9279fd146950'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.alter_column('departure_date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('departure_time',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.alter_column('departure_time',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('departure_date',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###
