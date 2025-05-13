"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""



class Miner:
    name = ""
    alive = True
    sleepiness = 0
    thirst = 0
    hunger = 0
    whisky = 0
    gold = 0
    previous_sleepiness = 0
    previous_thirst = 0
    previous_hunger = 0
    previous_whisky = 0
    previous_gold = 0

    def __init__(self, name) -> None:
        if name == "":
            self.name = "Morris"
        else:
            self.name = name

    def __str__(self) -> str:
        return self.name

    def update_previous_stats(self) -> None:
        self.previous_hunger = self.hunger
        self.previous_thirst = self.thirst
        self.previous_sleepiness = self.sleepiness
        self.previous_whisky = self.whisky
        self.previous_gold = self.gold

    def clamp_stats(self) -> None:
        self.hunger = max(0, self.hunger)
        self.thirst = max(0, self.thirst)
        self.sleepiness = max(0, self.sleepiness)
        self.whisky = max(0, self.whisky)
        self.gold = max(0, self.gold)

    def get_day_start_message(self) -> str:
        # major status updates
        if self.hunger >= 75:
            if self.thirst >= 75:
                if self.sleepiness >= 75:
                    return f"{self.name} could really use a vacation..."
                return f"{self.name} is looking a bit malnourished."
            if self.sleepiness >= 75:
                return f"{self.name} ate a hallucinated steak."
            return f"{self.name} could really use a hallucinated steak."
        if self.thirst >= 75:
            if self.sleepiness >= 75:
                return f"{self.name} keeps on seeing mirages."
            return f"{self.name} is audibly hoarse."
        if self.sleepiness >= 75:
            return f"{self.name}'s eyes can hardly keep themselves open."

        # minor status updates
        if self.hunger >= 40:
            if self.thirst >= 40:
                if self.sleepiness >= 40:
                    return f"{self.name} looks a bit worse for wear."
                return f"{self.name} could use a snack."
            if self.sleepiness >= 40:
                return f"{self.name} keeps nodding off while thinking about roast chicken."
            return f"{self.name}'s stomach rumbles."
        if self.thirst >= 40:
            if self.sleepiness >= 40:
                return f"{self.name} has a faint headache."
            return f"{self.name}'s throat is dry."
        if self.sleepiness >= 40:
            return f"{self.name}'s eyes have bags under them."

        # everything is right as rain
        return f"{self.name} is ready for anything."

    def announce_day_start(self) -> None:
        print(self.get_day_start_message())

    # eat: hunger -= 20, thirst -= 5, sleepiness += 5, whisky += 0, gold -= 2
    # drink: hunger -= 1, thirst -= 15, sleepiness += 5, whisky -= 1, gold += 0
    # sleep: hunger += 1, thirst += 1, sleepiness -= 10, whisky += 0, gold += 0
    # buy_whisky: hunger += 1, thirst += 1, sleepiness += 5, whisky += 1, gold -= 1
    # mine: hunger += 5, thirst += 5, sleepiness += 5, whisky += 0, gold += 5
    def eat(self) -> bool:
        if self.gold < 2:
            print(f"{self.name} can't afford food.")
            return False
        self.update_previous_stats()
        self.hunger -= 20
        self.thirst -= 5
        self.sleepiness += 5
        self.gold -= 2
        self.clamp_stats()
        print(f"{self.name} ate food.")
        self.announce_stat_changes()
        self.check_death()
        return True

    def drink(self) -> bool:
        if self.whisky < 1:
            print(f"{self.name} doesn't have any whisky.")
            return False
        self.update_previous_stats()
        self.hunger -= 1
        self.thirst -= 15
        self.sleepiness += 5
        self.whisky -= 1
        self.clamp_stats()
        print(f"{self.name} drank some whisky.")
        self.announce_stat_changes()
        self.check_death()
        return True

    def sleep(self) -> bool:
        self.update_previous_stats()
        self.hunger += 1
        self.thirst += 1
        self.sleepiness -= 10
        self.clamp_stats()
        print(f"{self.name} slept.")
        self.announce_stat_changes()
        self.check_death()
        return True

    def buy_whisky(self) -> bool:
        if self.gold < 1:
            print(f"{self.name} can't afford whisky.")
            return False
        if self.whisky >= 10:
            print(f"{self.name} is carrying too much whisky.")
            return False
        self.update_previous_stats()
        self.hunger += 1
        self.thirst += 1
        self.sleepiness += 5
        self.whisky += 1
        self.gold -= 1
        self.clamp_stats()
        print(f"{self.name} bought some whisky.")
        self.announce_stat_changes()
        self.check_death()
        return True

    def mine(self) -> bool:
        self.update_previous_stats()
        self.hunger += 5
        self.thirst += 5
        self.sleepiness += 5
        self.gold += 5
        self.clamp_stats()
        print(f"{self.name} went mining.")
        self.announce_stat_changes()
        self.check_death()
        return True

    @staticmethod
    def announce_stat(stat_name, current, previous, lethal = False) -> None:
        change = current - previous
        printed_string = f"{stat_name}: {current}"
        if change > 0:
            printed_string = f"{stat_name}: {previous} +{change} > {current}"
        elif change < 0:
            printed_string = f"{stat_name}: {previous} {change} > {current}"
        if lethal and current >= 100:
            print(f"{printed_string} !!!")
        else:
            print(printed_string)

    def announce_stat_changes(self) -> None:
        Miner.announce_stat("Hunger", self.hunger, self.previous_hunger, True)
        Miner.announce_stat("Thirst", self.thirst, self.previous_thirst, True)
        Miner.announce_stat("Sleepiness", self.sleepiness, self.previous_sleepiness, True)
        Miner.announce_stat("Whisky", self.whisky, self.previous_whisky)
        Miner.announce_stat("Gold", self.gold, self.previous_gold)

    def is_dead(self) -> bool:
        return self.sleepiness >= 100 or self.thirst >= 100 or self.hunger >= 100

    def get_death_cause(self) -> str:
        if self.hunger >= 100:
            if self.thirst >= 100:
                if self.sleepiness >= 100:
                    return "everything"
                return "malnutrition"
            if self.sleepiness >= 100:
                return "hunger and overexertion"
            return "hunger"
        if self.thirst >= 100:
            if self.sleepiness >= 100:
                return "thirst and overexertion"
            return "thirst"
        if self.sleepiness >= 100:
            return "overexertion"
        return "mysterious causes"

    def announce_death(self) -> None:
        print(f"{self.name} died of {self.get_death_cause()}.")

    def die(self) -> None:
        print("YOU DIED!")
        self.announce_death()
        self.alive = False

    def check_death(self) -> None:
        if self.is_dead():
            self.die()


def main() -> None:
    player = Miner(input("Choose a name. (Leave blank to use the default: Morris.)\n"))
    days = 0

    while player.alive:
        days += 1
        print(f"Day {days}")
        player.announce_day_start()
        action_successful = False

        while not action_successful:
            action = input(f"What should {player.name} do? (eat, drink, sleep, buy whisky, or mine; stats to view stats; exit to give up)\n")
            if action == "eat":
                action_successful = player.eat()
            elif action == "e":
                action_successful = player.eat()
            elif action == "drink":
                action_successful = player.drink()
            elif action == "d":
                action_successful = player.drink()
            elif action == "sleep":
                action_successful = player.sleep()
            elif action == "s":
                action_successful = player.sleep()
            elif action == "buy whisky":
                action_successful = player.buy_whisky()
            elif action == "bw":
                action_successful = player.buy_whisky()
            elif action == "buy":
                action_successful = player.buy_whisky()
            elif action == "b":
                action_successful = player.buy_whisky()
            elif action == "whisky":
                action_successful = player.buy_whisky()
            elif action == "w":
                action_successful = player.buy_whisky()
            elif action == "mine":
                action_successful = player.mine()
            elif action == "m":
                action_successful = player.mine()
            elif action == "stats":
                player.update_previous_stats()
                player.announce_stat_changes()
                print(f"Survived for {days} days.")
            elif action == "stat":
                player.update_previous_stats()
                player.announce_stat_changes()
                print(f"Survived for {days} days.")
            elif action == "st":
                player.update_previous_stats()
                player.announce_stat_changes()
                print(f"Survived for {days} days.")
            elif action == "exit":
                action_successful = True
                player.die()
    print(f"You survived {days} days.")
    input("Press ENTER to exit.")


if __name__ == "__main__":
    main()
