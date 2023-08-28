"""Initial migration

Revision ID: cd46ef39591e
Revises: 
Create Date: 2023-08-25 12:33:54.241113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd46ef39591e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.Column('mobile_no', sa.String(length=100), nullable=True),
    sa.Column('bank_name', sa.String(length=100), nullable=True),
    sa.Column('branch', sa.String(length=100), nullable=True),
    sa.Column('ifsc_code', sa.String(length=100), nullable=True),
    sa.Column('account_number', sa.String(length=100), nullable=True),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('tin', sa.String(length=100), nullable=True),
    sa.Column('pan_number', sa.String(length=100), nullable=True),
    sa.Column('metamask_address', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile_no'),
    sa.UniqueConstraint('username')
    )
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.String(length=100), nullable=True),
    sa.Column('total_amount', sa.Float(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=False),
    sa.Column('buyer_metamask_address', sa.String(length=100), nullable=False),
    sa.Column('pdf_url', sa.String(length=200), nullable=True),
    sa.Column('approval_status', sa.Boolean(), nullable=True),
    sa.Column('metamask_address', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['buyer_metamask_address'], ['user.metamask_address'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sent_for_approval',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('invoice', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('buyer_id', sa.Integer(), nullable=False),
    sa.Column('buyer_metamask_address', sa.String(length=100), nullable=False),
    sa.Column('approve_status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['buyer_metamask_address'], ['user.metamask_address'], ),
    sa.ForeignKeyConstraint(['invoice'], ['invoice.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sent_for_approval')
    op.drop_table('invoice')
    op.drop_table('user')
    # ### end Alembic commands ###
