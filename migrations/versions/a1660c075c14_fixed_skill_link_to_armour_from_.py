"""fixed skill link to armour from skillModel to skillRankModel

Revision ID: a1660c075c14
Revises: b8c6cdb3c9be
Create Date: 2025-03-29 17:27:56.769524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1660c075c14'
down_revision = 'b8c6cdb3c9be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill_model', schema=None) as batch_op:
        batch_op.drop_constraint('skill_model_armour_id_fkey', type_='foreignkey')
        batch_op.drop_column('armour_id')

    with op.batch_alter_table('skill_rank_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('armour_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'armour_model', ['armour_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill_rank_model', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('armour_id')

    with op.batch_alter_table('skill_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('armour_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('skill_model_armour_id_fkey', 'armour_model', ['armour_id'], ['id'])

    # ### end Alembic commands ###
