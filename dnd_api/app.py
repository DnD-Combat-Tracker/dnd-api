from flask import Flask, request
from MonsterGen import Monster, CR, random_trap, Npc, monster_loot, horde_loot

def create_app():

    app = Flask(__name__)

    @app.route('/monster')
    def monster():
        level = int(request.args['avg-level'])
        players = int(request.args['num-players'])
        difficulty = int(request.args['difficulty'])
        return Monster(CR.party_adapter(
            average_level=level,
            num_players=players,
            difficulty=difficulty,
        )).to_dict()

    @app.route('/monster-cr-type')
    def monster_cr():
        return Monster(
            int(request.args['cr']),
            request.args['type'],
        ).to_dict()

    @app.route('/treasure')
    def treasure():
        return monster_loot(int(request.args['cr'])).to_dict()

    @app.route('/treasure-horde')
    def treasure_horde():
        return horde_loot(int(request.args['cr'])).to_dict()

    @app.route('/trap')
    def trap():
        return random_trap(int(request.args['cr'])).to_dict()

    @app.route('/trap-type')
    def trap_type():
        cr = int(request.args['cr'])
        damage_type = request.args['type']
        return random_trap(cr, damage_type).to_dict()

    @app.route('/npc')
    def npc():
        return Npc().to_dict()

    return app
    
if __name__ == "__main__":
    create_app().run()