"""Amongus."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, colour: str, role: str, tasks: int = 10, protected: bool = False):
        """Initialize crewmate object."""
        self.colour = colour.title()
        self.role = self._add_role(role).title()
        self.tasks = tasks
        self.protected = protected

    def _add_role(self, role):
        """Add a role to the crewmate object."""
        role_options = ["Crewmate", "Sheriff", "Guardian Angel", "Altruist"]
        if role.title() in role_options:
            return role
        return "Crewmate"  # kui mingi muu sodi annab crewmate rolliks

    def complete_task(self):
        """Complete crewmate task."""
        if self.tasks > 0:
            self.tasks -= 1

    def __repr__(self):
        """Return in this format."""
        return f"{self.colour}, role: {self.role}, tasks left: {self.tasks}."


class Impostor:
    """Impostor class."""

    def __init__(self, colour, kills: int = 0):
        """Initialize impostor object w kills set to 0 at start."""
        self.colour = colour.title()
        self.kills = kills

    def __repr__(self):
        """Return in this format."""
        return f"Impostor {self.colour}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        """Initialize spaceship."""
        self.crewmates = []
        self.impostors = []
        self.dead_players = []

    def add_crewmate(self, crewmate):  # lisab tehtud crewmate laeva
        """Lisa crewmate unique to colour."""
        if isinstance(crewmate, Crewmate):
            used_colours = [col.colour.lower() for col in self.crewmates + self.impostors]  # col.colour.lower col for loop jaoks colour on crewmate objekt omadus teeb selle loweriks
            # vaatab labi nii impostorid kui crewmateid
            if crewmate.colour.lower() not in used_colours:
                self.crewmates.append(crewmate)

    def add_impostor(self, impostor):  # lisab tehtud impostori laeva
        """Lisa impostor colour sensitive."""
        if isinstance(impostor, Impostor):
            used_colours = [col.colour.lower() for col in self.crewmates + self.impostors]
            if impostor.colour.lower() not in used_colours and len(self.impostors) < 3:
                self.impostors.append(impostor)

    def kill_crewmate(self, impostor, crewmate_colour):
        """Kill a crewmate increase the kill count and move the dead crewmate to the other list."""
        if isinstance(impostor, Impostor):  # kas sisend on impostor
            for crewmate in self.crewmates:  # checki labi koik crewmateid otsi oige
                if crewmate.colour.lower() == crewmate_colour.lower():  # kui leiab crewmate objektidest matchiva varviga crewmate (case insensitive)
                    self.crewmates.remove(crewmate)  # remove the dead one
                    self.dead_players.append(crewmate)  # lisa ta dead listi
                    impostor.kills += 1  # lisa selle impostori killile uks
                    return  # lopeta check

    def revive_crewmate(self, saviour, the_dead_one):
        """Revive a crewmate."""
        if isinstance(saviour, Crewmate) and isinstance(the_dead_one, Crewmate):  # molemad on crew
            if saviour.role == "Altruist" and saviour in self.crewmates and the_dead_one in self.dead_players:  # paastja on alturist on elus ja teine on surnud
                self.dead_players.remove(the_dead_one)
                self.crewmates.append(the_dead_one)
                self.crewmates.remove(saviour)  # kui savib saab ise surma
                self.dead_players.append(saviour)

    def get_role_of_player(self, player_colour):
        """Get player role for both roles."""
        for crewmate in self.crewmates:  # algul otsime crewmate seast
            if crewmate.colour.lower() == player_colour.lower():  # case insensitive
                return crewmate.role  # returni selle varviga seotud objekti roll

        for impostor in self.impostors:  # impostor seast
            if impostor.colour.lower() == player_colour.lower():
                return "Impostor"

    def protect_crewmate(self, protector, protected_colour):
        """Protect a crewmate ainult uks saab olla korraga."""
        if isinstance(protector, Crewmate) and isinstance(protected_colour, Crewmate):
            if protector.role == "Guardian Angel" and protector.colour.lower() in self.dead_players:  # protector peab olema surnud ja guardian angel et kaitsta
                for crewmate in self.crewmates:  # otsib kas keegi juba on protected
                    if crewmate.protected is True:
                        return
                protected_colour.protected = True  # kui ei siis protectib teda

    def kill_impostor(self):
        """Sheriff saab impostor tappa."""
        pass

    def sort_crewmates_by_tasks(self):
        """Sort crewmates by tasks."""
        pass

    def sort_impostors_by_kills(self):
        """Sort impostors by kills."""
        pass

    def get_regular_crewmates(self):
        """Get regular crewmates."""
        regular_crewmates = []  # as a list kuna ma muidu sai koguaeg 1 tagasi aint
        for crewmate in self.crewmates:
            if crewmate.role == "Crewmate":
                regular_crewmates.append(crewmate)
        return regular_crewmates

    def get_dead_players(self):
        """Get dead players."""
        return self.dead_players

    def get_crewmate_list(self):
        """Get all crewmates."""
        return self.crewmates

    def get_impostor_list(self):
        """Get all impostors."""
        return self.impostors

    def get_crewmate_with_most_tasks_done(self):
        """Get crewmate with most tasks done."""
        pass

    def get_impostor_with_most_kills(self):
        """Get impostor with most kills."""
        pass


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> [Impostor Orange, kills: 0., Impostor Black, kills: 0., Impostor Purple, kills: 0.]
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> [Yellow, role: Guardian Angel, tasks left: 4.]
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> [Red, role: Crewmate, tasks left: 9., White, role: Crewmate, tasks left: 10.]
    print(spaceship.sort_impostors_by_kills())  # -> [Impostor Purple, kills: 2., Impostor Orange, kills: 1., Impostor Black, kills: 0.]
    print(spaceship.get_regular_crewmates())  # -> [White, role: Crewmate, tasks left: 10., Red, role: Crewmate, tasks left: 9.]
