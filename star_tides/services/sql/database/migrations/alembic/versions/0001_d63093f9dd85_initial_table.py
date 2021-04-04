"""0001_initial_table

Revision ID: d63093f9dd85
Revises: 
Create Date: 2021-03-28 17:50:24.873822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd63093f9dd85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password_hash', sa.LargeBinary, nullable=True)
    )


def downgrade():
    op.drop_table('users')
