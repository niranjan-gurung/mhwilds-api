from flask_restful import fields

slot_fields = {
  'id': fields.Integer,
  'level': fields.Integer,
  'armour_id': fields.Integer
}

skill_rank_fields = {
  'id': fields.Integer,
  'level': fields.Integer,
  'skill_id': fields.Integer,
  'desc': fields.String
}

skills_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'type': fields.String,
  'desc': fields.String,
  'ranks': fields.List(fields.Nested(skill_rank_fields))
}

armour_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'slug': fields.String,
  'type': fields.String,
  'rank': fields.String,
  'rarity': fields.Integer,
  'slots': fields.List(fields.Nested(slot_fields)),
  'skills': fields.List(fields.Nested(skill_rank_fields))
}