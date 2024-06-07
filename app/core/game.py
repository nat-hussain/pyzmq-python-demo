import pygame
import zmq

class Game:
    """Game class that initializes the game and runs the game loop
        It uses pygame to create a window and display the counter value
    """
    def __init__(self,host="localhost",port=5002):
        """init class

        Args:
            host (str, optional): zmq host. Defaults to "localhost".
            port (int, optional): zmq port. Defaults to 5002.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PyZMQ Python Demo")
        
        green = (0, 255, 0)
        blue = (0, 0, 128)
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('0', True, green, blue)
        self.textRect = self.text.get_rect()
        self.textRect.center = (800 // 2, 600 // 2)
        
        self.running = True
               
        self.init_zmq(host,port)
        
    def init_zmq(self,host,port):
        """Init zmq socket

        Args:
            host (str): zmq host
            port (int): zmq port
        """
        self.host = host
        self.port = port
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect(f"tcp://{self.host}:{self.port}")        
        self.socket.subscribe("counter")
        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)

    def run(self):
        """game loop that runs the game and listens to zmq socket for messages
        """
        green = (0, 255, 0)
        blue = (0, 0, 128)
        msg="0"
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.text, self.textRect)
            pygame.display.flip()
            
            evts=dict(self.poller.poll(timeout =0))
            if self.socket in evts:
                topic = self.socket.recv_string()
                msg = self.socket.recv_string()
                print(f"Topic received: {topic}")
                print(f"Message received: {msg}")
            self.text = self.font.render(msg, True, green, blue)
            

        pygame.quit()
        print("Game process finished...")
        
if __name__ == "__main__":
    game = Game()
    game.run()