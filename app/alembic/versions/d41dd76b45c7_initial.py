from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd41dd76b45c7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('incidents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('finder', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_incidents'))
    )
    op.create_index(op.f('ix_incidents_date_time'), 'incidents', ['date_time'], unique=False)
    op.create_index(op.f('ix_incidents_finder'), 'incidents', ['finder'], unique=False)
    op.create_index('ix_incidents_finder_date_time', 'incidents', ['finder', 'date_time'], unique=False)
    op.create_index(op.f('ix_incidents_id'), 'incidents', ['id'], unique=False)
    op.create_index(op.f('ix_incidents_status'), 'incidents', ['status'], unique=False)
    op.create_index('ix_incidents_status_date_time', 'incidents', ['status', 'date_time'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_incidents_status_date_time', table_name='incidents')
    op.drop_index(op.f('ix_incidents_status'), table_name='incidents')
    op.drop_index(op.f('ix_incidents_id'), table_name='incidents')
    op.drop_index('ix_incidents_finder_date_time', table_name='incidents')
    op.drop_index(op.f('ix_incidents_finder'), table_name='incidents')
    op.drop_index(op.f('ix_incidents_date_time'), table_name='incidents')
    op.drop_table('incidents')
