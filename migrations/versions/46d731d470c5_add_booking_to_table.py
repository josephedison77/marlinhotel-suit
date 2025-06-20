"""add Booking to table

Revision ID: 46d731d470c5
Revises: f1a6aab5bae6
Create Date: 2025-06-01 07:46:45.924593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46d731d470c5'
down_revision = 'f1a6aab5bae6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reminder_sent', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('checked_out', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_column('checked_out')
        batch_op.drop_column('reminder_sent')

    # ### end Alembic commands ###
