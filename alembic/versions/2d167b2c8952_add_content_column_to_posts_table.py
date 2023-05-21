"""add content column to posts table

Revision ID: 2d167b2c8952
Revises: a98aa2ba2fbb
Create Date: 2023-05-21 10:15:32.771250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2d167b2c8952"
down_revision = "a98aa2ba2fbb"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
