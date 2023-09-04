"""Add reset_token column to User

Revision ID: e0334740570d
Revises: 4be089fa241d
Create Date: 2023-09-04 11:42:22.434309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0334740570d'
down_revision: Union[str, None] = '4be089fa241d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    op.add_column('users', sa.Column('reset_token', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('street_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('street_number', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('complex_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('complex_number', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('area', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('price', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('bedrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bathrooms', sa.NUMERIC(precision=3, scale=1), autoincrement=False, nullable=True),
    sa.Column('garages', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('swimming_pool', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('garden_flat', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('study', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('ground_floor', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('pet_friendly', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('link', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('link_display', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('note', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='properties_pkey')
    )
    # ### end Alembic commands ###