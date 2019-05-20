from interface.start_menu import StartMenu

class Application: 
    @classmethod
    def start(csl):
       StartMenu.run()

if __name__ == "__main__":
    Application.start()