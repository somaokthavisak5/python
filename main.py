class NetflixApp:
    def __init__(self):
        self.shows = {}
        self.current_show = None

    def create_show(self, show_name):
        self.shows[show_name] = []
        print(f"Show '{show_name}' created.")

    def add_episode_to_show(self, show_name, episode):
        if show_name in self.shows:
            self.shows[show_name].append(episode)
            print(f"Added '{episode}' to show '{show_name}'")
        else:
            print(f"Show '{show_name}' not found")

    def play_episode(self, episode):
        self.current_show = episode
        print(f"Now playing: '{episode}'")

    def show_current_episode(self):
        if self.current_show:
            print(f"Currently playing: '{self.current_show}'")
        else:
            print("No episode is currently playing.")

netflix = NetflixApp()

while True:
    print("Available commands: create show, add episode, play episode, current episode, exit")
    command = input("Enter a command: ")

    if command == "create show":
        show_name = input("Enter show name: ")
        netflix.create_show(show_name)
    elif command == "add episode":
        show_name = input("Enter show name: ")
        episode = input("Enter episode name: ")
        netflix.add_episode_to_show(show_name, episode)
    elif command == "play episode":
        episode = input("Enter episode name: ")
        netflix.play_episode(episode)
    elif command == "current episode":
        netflix.show_current_episode()
    elif command == "exit":
        print("Exiting the Netflix app. Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")
