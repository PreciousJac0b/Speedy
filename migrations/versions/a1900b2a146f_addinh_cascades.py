"""Addinh cascades

Revision ID: a1900b2a146f
Revises: 9d472b37e5e2
Create Date: 2023-09-14 15:40:58.784609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1900b2a146f'
down_revision = '9d472b37e5e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_account')
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.alter_column('account_pin',
               existing_type=sa.VARCHAR(length=4),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.alter_column('account_pin',
               existing_type=sa.VARCHAR(length=4),
               nullable=True)

    op.create_table('_alembic_tmp_account',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('cus_id', sa.INTEGER(), nullable=True),
    sa.Column('account_number', sa.VARCHAR(length=100), nullable=False),
    sa.Column('acc_type', sa.VARCHAR(length=240), nullable=True),
    sa.Column('balance', sa.INTEGER(), nullable=True),
    sa.Column('bank_name', sa.VARCHAR(length=240), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('account_pin', sa.VARCHAR(length=4), nullable=False),
    sa.ForeignKeyConstraint(['cus_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###