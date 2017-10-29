from flask_restplus import Namespace, Resource, fields


api = Namespace('items', description='Items related operations')

item = api.model('Item', {
    'id': fields.Integer(readOnly=True, description='The item identifier'),
    'name': fields.String(required=True, description='The item name'),
})


ITEMS = [
    {'id': 0, 'name': 'thing'},
]


parser = api.parser()
parser.add_argument('name', type=str, required=True, help='The item name', location='form')


@api.route('/')
class Items(Resource):
    @api.doc('list_items')
    @api.marshal_list_with(item)
    def get(self):
        """ List all items """
        return ITEMS

    @api.doc('post_item', parser=parser)
    @api.marshal_with(item, code=201)
    def post(self):
        """ Create an item """
        args = parser.parse_args()
        name = args['name']
        for item in ITEMS:
            if item['name'] == name:
                api.abort(404)
                break
        else:
            new_item = {'id': len(ITEMS), 'name': name}
            ITEMS.append(new_item)
            return new_item, 201


@api.route('/<int:id>')
@api.param('id', 'The item identifier')
@api.response(404, 'Item not found')
class Item(Resource):
    @api.doc('get_item')
    @api.marshal_with(item)
    def get(self, id):
        """ Fetch an item given its identifier """
        for item in ITEMS:
            if item['id'] == id:
                return item
        api.abort(404)
