class Game():
    def __init__(self, window_name="Caracal Window", x=400,y=640):
        import pygame
        self.pygame = pygame
        self.window = pygame.display
        self.window_name = window_name
        self.x = x
        self.y = y
        self.before_update=[]
        self.after_update=[]
    

    

    def preflip_tasks(self):
        #accepts functions as tasks to be handled BEFORE updating frames, in a list.
        for task in self.before_update:
            task()
    
    def postflip_tasks(self):
        #accepts functions as tasks to be handled AFTER updating frames, in a list.
        for task in self.after_update:
            task()

    def run(self):
        pygame = self.pygame
        self.window.set_mode((self.x,self.y))
        self.window.set_caption(self.window_name)
        while True:
            self.preflip_tasks()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

