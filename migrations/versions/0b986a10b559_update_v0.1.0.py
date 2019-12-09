"""empty message

Revision ID: 0b986a10b559
Revises: 837eddb8eee0
Create Date: 2019-12-09 08:15:42.068490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b986a10b559'
down_revision = '837eddb8eee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection_items', sa.Column('compressed_file', sa.String(), nullable=True))
    op.drop_constraint('composite_function_schemas_id_key', 'composite_function_schemas', type_='unique')
    op.create_index('idx_tiles_geom', 'tiles', ['geom'], unique=False, postgres_using='gist')
    op.create_index('idx_tiles_geom_wgs84', 'tiles', ['geom_wgs84'], unique=False, postgres_using='gist')
    op.drop_index('ix_tiles_geom_wgs84', table_name='tiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_tiles_geom_wgs84', 'tiles', ['geom_wgs84'], unique=False)
    op.drop_index('idx_tiles_geom_wgs84', table_name='tiles')
    op.drop_index('idx_tiles_geom', table_name='tiles')
    op.create_unique_constraint('composite_function_schemas_id_key', 'composite_function_schemas', ['id'])
    op.drop_column('collection_items', 'compressed_file')
    # ### end Alembic commands ###