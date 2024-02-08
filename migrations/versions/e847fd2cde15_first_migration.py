"""First migration

Revision ID: e847fd2cde15
Revises: 
Create Date: 2024-02-07 16:37:36.495067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e847fd2cde15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_pdf')
    op.add_column('usuario', sa.Column('edita', sa.String(length=5), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'edita')
    op.create_table('file_pdf',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('file', sa.VARCHAR(length=100), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###