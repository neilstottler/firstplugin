from events import Event
from players.entity import Player
from players.helpers import index_from_userid
from messages import SayText2
from filters.players import PlayerIter
from commands.typed import TypedSayCommand, TypedClientCommand


# Extra amount of health every player should get on spawn
EXTRA_HP = 25

def load():
    SayText2('Plugin has been loaded successfully!').send()

def unload():
    SayText2('Plugin has been unloaded successfully!').send()



# test command
@TypedSayCommand("!test")
@TypedClientCommand("sp_test")
def something(command_info):
    SayText2("testing 123 with admin permissions").send()