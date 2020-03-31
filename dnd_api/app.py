from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/monsters')
    def hello_world_monster():
      return 'Hello, monsters!'

    @app.route('/treasure')
    def hello_world_treasure():
      return 'Hello, treasure!'

    @app.route('/trap')
    def hello_world_trap():
      return 'Hello, trap!'

    @app.route('/npc')
    def hello_world_npc():
      return 'Hello, NPC!'

    return app

if __name__ == "__main__":
    app = create_app()