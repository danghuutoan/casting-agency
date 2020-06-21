"""empty message

Revision ID: 3a7d4bb6e87a
Revises: 08b2ffcd35ac
Create Date: 2020-06-21 22:21:30.582488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a7d4bb6e87a'
down_revision = '08b2ffcd35ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actor', sa.Column('gender_id', sa.Integer(), nullable=True))
    op.drop_constraint('actor_gender_fkey', 'actor', type_='foreignkey')
    op.create_foreign_key(None, 'actor', 'gender', ['gender_id'], ['id'])
    op.drop_column('actor', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actor', sa.Column('gender', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'actor', type_='foreignkey')
    op.create_foreign_key('actor_gender_fkey', 'actor', 'gender', ['gender'], ['id'])
    op.drop_column('actor', 'gender_id')
    # ### end Alembic commands ###