"""video_keys

Revision ID: 18922c5b115
Revises: 169fab57fdcf
Create Date: 2015-05-27 23:16:28.712472

"""

# revision identifiers, used by Alembic.
revision = '18922c5b115'
down_revision = '169fab57fdcf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('key', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'key')
    ### end Alembic commands ###
