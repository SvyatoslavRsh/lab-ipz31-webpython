"""empty message

Revision ID: e941f5788e14
Revises: d02b5e7854f3
Create Date: 2021-12-04 19:34:42.131946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e941f5788e14'
down_revision = 'd02b5e7854f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_number', sa.Integer(), nullable=False),
    sa.Column('point_departure', sa.String(length=50), nullable=False),
    sa.Column('point_destination', sa.String(length=50), nullable=False),
    sa.Column('departure_date', sa.String(length=50), nullable=False),
    sa.Column('departure_time', sa.String(length=50), nullable=False),
    sa.Column('travel_time', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('Internal', 'International', name='routetype'), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flight')
    # ### end Alembic commands ###
