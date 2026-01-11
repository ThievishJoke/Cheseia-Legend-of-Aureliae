from language.localization import translate

class AureliaeDialogue:
    def talk(self, player):
        name = translate("dialogue.aureliae.Aureliae.name")

        p_name = player.name

        print(name + translate("dialogue.aureliae.Aureliae.first_greeting", player=p_name))
        print(name + translate("dialogue.aureliae.Aureliae.self_introduction"))
        print(name + translate("dialogue.aureliae.Aureliae.farewell", player=p_name))