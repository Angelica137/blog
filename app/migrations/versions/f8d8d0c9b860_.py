"""empty message

Revision ID: f8d8d0c9b860
Revises: 1abd2f0bac82
Create Date: 2020-08-26 17:29:42.074107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8d8d0c9b860'
down_revision = '1abd2f0bac82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.Column('modified_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_has', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('entry_tags',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('entry_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry_tags')
    op.drop_table('user')
    op.drop_table('tag')
    op.drop_table('entry')
    # ### end Alembic commands ###
