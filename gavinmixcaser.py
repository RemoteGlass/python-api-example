from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class GavinMixcaser(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in mixcase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to mixcase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in mixcase
                             
        """
        text = request.args.get('text')
        textuppper = text.upper()
        textlowwer = text.lower()
        textmix = textuppper +" "+ textlowwer
        return {"text": textmix}, 200
      
class Gavinuppercaser(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in Lowercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to lowercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in lowercase
        """
        text = request.args.get('text')

        return {"text": text.upper()}, 200
    
class GavinLowercaser(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in Lowercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to lowercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in lowercase
        """
        text = request.args.get('text')

        return {"text": text.lower()}, 200
    


api.add_resource(GavinMixcaser, "/mixcase")
api.add_resource(Gavinuppercaser, "/uppercase")
api.add_resource(GavinLowercaser, "/Gavinlowercaser")


if __name__ == "__main__":
    app.run(debug=True)


