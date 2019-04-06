"""empty message

Revision ID: 35ebfab46a63
Revises: bca6cd934ce2
Create Date: 2018-10-14 06:54:33.682314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ebfab46a63'
down_revision = 'bca6cd934ce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('zu_cid', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'zu_cid')
    # ### end Alembic commands ###