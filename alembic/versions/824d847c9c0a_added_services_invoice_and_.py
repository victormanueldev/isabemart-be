"""Added services, invoice and servicesusers assoc

Revision ID: 824d847c9c0a
Revises: 80cf82d754b6
Create Date: 2023-05-17 08:38:09.141011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824d847c9c0a'
down_revision = '80cf82d754b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_invoiced', sa.Integer(), nullable=False),
    sa.Column('is_paid', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_invoice_id'), 'invoice', ['id'], unique=False)
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type', sa.String(), nullable=False),
    sa.Column('expected_date', sa.DateTime(), nullable=False),
    sa.Column('executed_date', sa.DateTime(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('observations', sa.String(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('headquarter_id', sa.Integer(), nullable=True),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['headquarter_id'], ['headquarter.id'], ),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_id'), 'service', ['id'], unique=False)
    op.create_index(op.f('ix_service_observations'), 'service', ['observations'], unique=False)
    op.create_index(op.f('ix_service_service_type'), 'service', ['service_type'], unique=False)
    op.create_table('serviceuser',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('service_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('serviceuser')
    op.drop_index(op.f('ix_service_service_type'), table_name='service')
    op.drop_index(op.f('ix_service_observations'), table_name='service')
    op.drop_index(op.f('ix_service_id'), table_name='service')
    op.drop_table('service')
    op.drop_index(op.f('ix_invoice_id'), table_name='invoice')
    op.drop_table('invoice')
    # ### end Alembic commands ###
