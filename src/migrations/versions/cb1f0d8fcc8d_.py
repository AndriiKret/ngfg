"""empty message

Revision ID: cb1f0d8fcc8d
Revises: 3e9cfc035061
Create Date: 2020-03-17 16:23:08.634604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb1f0d8fcc8d'
down_revision = '3e9cfc035061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fields', sa.Column('created', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('forms', sa.Column('created', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('groups', sa.Column('created', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.alter_column('settings_autocomplete', 'from_row',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('settings_autocomplete', 'to_row',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('settings_autocomplete', 'to_row',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('settings_autocomplete', 'from_row',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('groups', 'created')
    op.drop_column('forms', 'created')
    op.drop_column('fields', 'created')
    # ### end Alembic commands ###
