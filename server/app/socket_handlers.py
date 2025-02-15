# This will be changed to more structured code in the future. For now, we will keep it simple.
from flask import request
from flask_socketio import SocketIO
from .game import TicTacToe

socketio = SocketIO()

players = []
game: TicTacToe = None

@socketio.on('connect')
def connect():
    print('Client connected')
    players.append(request.sid)
    print(f'Players: {players}')

    if len(players) == 2:
        global game
        game = TicTacToe()
        print('Game started')
        socketio.emit('start', {
            'o': players[0],
            'x': players[1]
        })

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
    players.remove(request.sid)
    print(f'Players: {players}')

@socketio.on('event')
def handle_my_custom_event(json):
    print('received data: ' + str(json))

@socketio.on('move')
def move(data):
    try:
        player = players.index(request.sid)
    except ValueError:
        print(f'Player {player} not found')
        return
    
    if game is None:
        print('Game not started')
        return
    
    if game.o_to_move == player:
        print('Not your turn')
        return

    print(player, request.sid)
    if game.move(int(data['x']), int(data['y'])):
        print('Move successful')
        winner = game.check_winner()
        socketio.emit('state', {
            'board': game.board,
            'o_to_move': game.o_to_move
        })
        if winner > 0:
            # print(f'Player {players[winner-1]} wins')
            socketio.emit('winner', winner)
            