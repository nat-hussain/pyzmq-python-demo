import multiprocessing
import time
from core.game import Game
import zmq


def counter(host,port):
    """counter process that sends a counter to the zmq socket

    Args:
        host (str): zmq host
        port (int): zmq port
    """
    print("Counter process started...")
    i = 0
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect(f"tcp://{host}:{port}")
    
    while True:
        i += 1
        print(f"Counter: {i}")
        time.sleep(0.5)
        if(i==10):
            i = 0
        socket.send_string("counter",zmq.SNDMORE)
        socket.send_string(str(i))

def game(host,port):
    """game process that calls the Game class and runs the game

    Args:
        host (str): zmq host
        port (int): zmq port
    """
    print("Game process started...")
    game = Game(host=host,port=port)
    game.run()


def main():
    print("Init pyzmq demo...")
    
    context = zmq.Context()
    socket_sub = context.socket(zmq.XSUB)
    socket_pub = context.socket(zmq.XPUB)
    socket_sub.bind(f"tcp://*:5001")
    socket_pub.bind(f"tcp://*:5002")
    
    counter_process = multiprocessing.Process(target=counter, args=("localhost",5001))
    game_process = multiprocessing.Process(target=game, args=("localhost",5002))
    
    counter_process.start()
    game_process.start()
    
    
    
    zmq.proxy(socket_sub,socket_pub)  # connect subscribers to publishers
    
    
    counter_process.join()
    game_process.join()


if __name__ == "__main__":
    main()