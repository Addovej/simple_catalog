from flask import current_app as app
from flask import request, url_for
from flask_restful import Api
from flasgger import SwaggerView

from app.models import Product
from app.schemes import ProductSchema
from app.utils import response

api = Api(app, prefix='/api')


@api.resource('/')
class MainView(SwaggerView):
    responses = {
        200: {
            'description': 'Working message',
            'examples': {'response': {'message': 'Service is works'}}
        }
    }

    def get(self):
        """
            Check service
            Returning a success message.
        """

        return response('Service is works', 200)


@api.resource('/products', endpoint='api.products')
class ProductView(SwaggerView):
    parameters = [
        {
            'name': 'producer',
            'in': 'query',
            'type': 'string',
            'description': 'A product producer name',
            'example': 'Name'
        },
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'description': 'Current page',
            'example': 1
        },
        {
            'name': 'per_page',
            'in': 'query',
            'type': 'integer',
            'description': 'Products per page',
            'example': 15
        },
    ]
    responses = {
        200: {
            'description': 'Products list',
            'schema': ProductSchema
        },
    }

    def get(self):
        """
            Get products
            ---
        """

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 15, type=int)
        base_query = Product.query.order_by('id')

        producer = request.args.get('producer')
        if producer:
            products = base_query.filter_by(
                producer=producer,
            )
        else:
            products = base_query
        pagination = products.paginate(
            page, per_page
        )

        links_args = dict(request.args)
        links_args.update({'_external': True})
        _prev = None
        if pagination.has_prev:
            links_args.update({'page': page - 1})
            _prev = url_for('api.products', **links_args)
        _next = None
        if pagination.has_next:
            links_args.update({'page': page + 1})
            _next = url_for('api.products', **links_args)

        products_schema = ProductSchema(many=True)
        resp = {
            'prev': _prev,
            'next': _next,
            'total': pagination.total,
            'result': products_schema.dump(pagination.items),
        }

        return response(resp, 200)
