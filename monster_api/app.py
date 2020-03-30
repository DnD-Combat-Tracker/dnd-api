from flask import Flask, request, jsonify
from monster_api.monster_api_utils import monster_df

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def myfunc():
      return jsonify(monster_df.T.to_dict())

    return app

if __name__ == "__main__":
    app = create_app()