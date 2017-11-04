from flask_restplus import Namespace, Resource, fields

from database import db
from database.item import Item


api = Namespace('items', description='Items related operations')

item = api.model('Item', {
    'id': fields.Integer(readOnly=True, description='The item identifier'),
    'name': fields.String(required=True, description='The item name'),
})


parser = api.parser()
parser.add_argument('name', type=str, required=True, help='The item name', location='form')


@api.route('/')
class ItemsRes(Resource):
    @api.doc('list_items')
    @api.marshal_list_with(item)
    def get(self):
        """ List all items """
        return Item.query.all()

    @api.doc('post_item', parser=parser)
    @api.marshal_with(item, code=201)
    def post(self):
        """ Create an item """
        args = parser.parse_args()
        name = args['name']
        if Item.query.filter_by(name=name).first():
            api.abort(404)
        else:
            new_item = Item(name)
            db.session.add(new_item)
            db.session.commit()
            return new_item, 201


@api.route('/<int:id>')
@api.param('id', 'The item identifier')
@api.response(404, 'Item not found')
class ItemRes(Resource):
    @api.doc('get_item')
    @api.marshal_with(item)
    def get(self, id):
        """ Fetch an item given its identifier """
        db_item = Item.query.get(id)
        if db_item:
            return db_item
        api.abort(404)
