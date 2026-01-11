from language.localization import translate
from utility.formatting import Formatting as Format

class GuardDarelDialogue:
    def talk(self, player):
        name = translate("dialogue.guard.Guard_Darel.name")

        p_gender = player.gender

        print(name + translate("dialogue.guard.Guard_Darel.greeting", gender=p_gender))
        print(name + translate("dialogue.guard.Guard_Darel.quip1", gender=p_gender))
        print(name + f"{Format.ITALIC}{Format.UNDERLINE}"
              f"{translate('dialogue.guard.Guard_Darel.farewell')}{Format.RESET}")