"""Create posts table

Revision ID: a98aa2ba2fbb
Revises: 
Create Date: 2023-05-20 15:39:11.843486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a98aa2ba2fbb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column(
            "title",
            sa.String(),
            nullable=False,
        ),
    )

    pass


def downgrade():
    op.drop_table("posts")
    pass
