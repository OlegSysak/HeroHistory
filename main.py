import random
from time import sleep

from hero import Jojo, King, Kaban, Woolfs, Tooru, Diawollo, Bandit, BanditBoss, David, Arsen

hero1 = Jojo("Jojo", 15, 25, 15, "Saber", "Parrying with a counterattack", 20, "None", 0)
hero2 = Woolfs("Woolfs", 30, 0, 10, "Claws", "Aggression")
hero3 = Kaban("Kaban", 35, 30, 10, "Snout", "Aggression", "None", 0)
hero4 = King("King", 20, 20, 10, "King sword", "Very strong king ATTACK")
hero5 = Tooru("Tooru", 20, 20 ,20 , "Ice spear", "Icy spear extension", 25)
hero6 = Diawollo("Diawollo", 90, 230, 30, "Fire blades", "Fiery beasts", 70, "Stream of the tribe", 100)
hero7 = Bandit("Bandit", 10, 15, 15, "Knife", "None", 0, "None" )
hero8 = BanditBoss("Boss Bandit", 25, 10, 25, "Two-handed sword", "Oner", 30, "None", 0)
hero9 = David("David", 30, 40, 20, "Katana", "Piercing blow", 35, "None" , 0)
hero10 = Arsen("Arsen", 250, 200, 30, "Hammer", "Earth dragon", 110 , "Earthquake", 95)

print("*Kingdom of Chrom*")
sleep(1)
print("One day, a simple boy, Jojo, wants to get the Philosopher's Stone to gain knowledge about the creation of the universe, but his enemy, whom Jojo does not yet know, wants to oppose him...")
sleep(1)
print("Jojo went through many obstacles and got to the Chrom palace, he learned about the location of the Philosopher's Stone, but he was faced with a difficult choice, the king of Chrom (whose name was nameless, that is, he did not have a name) tortured his people, Jojo did not know whether it was necessary so much to risk a lot in order to save the common people. He was faced with a difficult choice... ")
sleep(1)
print("1) To risk oneself for the sake of others\n"
      "2) Follow the stone")
sleep(1)
while input() == "1":
    print("Jojo has decided not to give up on the common people and is ready to battle the king!!!")
    sleep(1)
    print("This battle will begin in the main court of the king")
    sleep(1)
    hero1.fight(hero4)
    sleep(1)
    print("How did the match go??")
    sleep(1)
    print("*if the victory is w, if the loss is l*")
    if input() == "w":
        print("After losing the king, Jojo went to collect special stones for the entrance to the altar, in which the philosopher's stone is to be placed.")
        sleep(1)
        hero1.__init__(name= "Jojo", health= 20, armor = 25, power = 20, weapon = "King sword", special = "Parrying with a counterattack", megapover = 20 , vievmagic = "None", magiceffect = 0)
        sleep(1)
        print("Health + 5, power +5.")
        sleep(1)
    else:
        print("Game over by losing, restart the game to play again.")
        sleep(1)

while input() == "2":
    print("Jojo decided not to risk his goal for the people…")
    sleep(1)
    print(
        "Jojo went to collect special stones for the entrance to the altar, which should contain the Philosopher's Stone.")
    sleep(1)
    hero1.__init__(name="Jojo", health=20, armor= 25, power=15, weapon="Saber", special="Parrying with a counterattack", megapover=20 , vievmagic = "None", magiceffect = 0)
    sleep(1)

print("There were 2 stones, Jojo knew their location but he didn't know the power of their guardians...: ")
sleep(1)
print("1) Road (Bonus Road)...\n"
      "2) Road (Bonus Road)...\n"
      "3) Road (Bonus Road))...\n"
      "*It will be possible to improve your character on each road*")
sleep(1)
while input() == "1":
    print("Oh no, on the first road, Jojo met a pack of wolves!!!")
    sleep(1)
    hero2.fight(hero1)
    sleep(1)
    print("if the victory is w, if the loss is l?")
    sleep(1)
    if input() == "w":
        print("Jojo was able to defeat a pack of wolves!!!")
        sleep(1)
        hero1.__init__(name = "Jojo", health= 15, armor= 25, power= 20, weapon= "Wolf tooth", special = "Parrying with a counterattack", megapover= 20, vievmagic = "None", magiceffect = 0)
        sleep(1)
        print("*Сила +5*")
    else:
        print("Game over by losing, restart the game to play again.")
        sleep(1)
while input() == "2":
    print("It looks like Jojo found a chest along the way, although it looked quite suspicious, but in the chest he found some beautiful armor.")
    sleep(1)
    hero1.__init__(name = "Jojo", health= 25, armor= 25, power= 15, weapon= "Saber", special = "Parrying with a counterattack", megapover= 20, vievmagic = "None", magiceffect = 0)
    sleep(1)
    print("armor +5")
while input() == "3":
    print("Kaban!!!!")
    sleep(1)
    hero3.fight(hero1)
    sleep(1)
    print("if the victory is w, if the loss is l?")
    if input() == "w":
        print("It seems that when splitting the boar, Jojo was able to get better armor!")
        sleep(1)
        hero1.__init__(name = "Jojo", health= 25, armor= 25, power= 15, weapon= "Boar's tooth", special = "Parrying with a counterattack", megapover= 20, vievmagic = "None", magiceffect = 0)
        sleep(1)
        print("armor +5")
    else:
        print("Game over by losing, restart the game to play again.")
        sleep(1)

print("Jojo reached the guardian of the first stone, near the little beauty stood one of the guardians of the stone, Tooru")
sleep(1)
print("He oppressed Tooru not only by force, but also morally.")
sleep(1)
print("Select an action: \n"
      "1) Surrender\n"
      "2) Fight")
while input() == 1:
    print("Jojo didn't have the strength to fight, Jojo chose to give up... He died a coward's death...")
    sleep(1)
    print("*If you want to try again, restart the game*")
else:
    print("Without another word, the battle began:")
    sleep(1)
    hero1.super(hero5)
    sleep(1)
    print("Jojo used the strongest attack that he hadn't used even when fighting the king")
    sleep(1)
    print("Tooru was able to resist and is already preparing his reception")
    sleep(1)
    hero5.super(hero1)
    sleep(1)
    hero1.fight(hero5)
    sleep(1)
    print("if the victory is w, if the loss is l?")
    if input() == "w":
        print("Jojo was able to defeat Tooru, but he was mortally wounded…")
        sleep(1)
        print("And then the stone unexpectedly healed and gave Jojo gigantic strength!!!")
        sleep(1)
        hero1.__init__(name="Jojo", health=100, armor=180, power=35, weapon="Ice spear", special="Ice spikes", megapover=70, vievmagic = "A large ice stream", magiceffect = 60)
    else:
        print("Jojo showed a decent fight, but could not win so much of the enemy.")
        sleep(1)
        print("*If you want to try again, restart the game*")
        sleep(1)
print("Jojo received gigantic strength and the gift of magic")
sleep(1)
print("It seems that it is time to test a new power, namely on a boar, which was already approaching the hero!")
sleep(1)
hero1.effect(hero3)
sleep(1)
hero1.fight(hero3)
sleep(1)
print("The power of magic is simply unmatched, now it's time to go for the last stone!!!")
sleep(1)

print("As mentioned earlier, Jojo knew where the stones were located, the second stone is located at the foot of the mountain")
sleep(1)
print("Reaching the foothills, Jojo met his enemy, the Diawollo!!!")
sleep(1)
print("Will Jojo win this battle? Choose the variant of the development of events, 1 or 2? It all depends on your luck.")
sleep(1)
if input() == "1":
    hero1.super(hero6)
    sleep(1)
    hero6.effect(hero1)
    sleep(1)
    hero6.effect(hero1)
    sleep(1)
    hero1.fight(hero6)
    sleep(1)
    print("The game is over with a loss, restart the game to play again.")
if input() == "2":
    hero1.effect(hero6)
    sleep(1)
    hero1.effect(hero6)
    sleep(1)
    hero6.super(hero1)
    sleep(1)
    hero1.fight(hero6)
    sleep(1)
    print("*you guessed it!!!*")
    sleep(1)
    print("Jojo was able to win this duel")
    sleep(1)
    print("Now that all the stones are found, it's time to open the portal, which is located on one of the three peaks of the mountain")
    sleep(1)

    print("But before that, you need to choose an improvement, namely which stone to use: \n"
          "1) Tooru \n"
          "2) Diawollo")
    if input() == "1":
        hero1.__init__(name="Jojo", health=180, armor=200, power=45, weapon="Ice spear", special="Attack dis", megapover=135,
                       vievmagic="Mass freezing", magiceffect=110)
        sleep(1)
        print("You have chosen Tooru")
    if input() == "2":
        hero1.__init__(name="Jojo", health=180, armor=120, power=55, weapon="Fire blades", special="Speed", megapover=135,
                       vievmagic="Ice", magiceffect=130)
        print("you chose Diawollo")
        sleep(1)

print("As Jojo climbed the mountain, he saw a strange man...")
sleep(1)
hero7.fight(hero9)
sleep(1)
hero8.super(hero9)
sleep(1)
hero9.super(hero8)
sleep(1)
print("David is Jojo's old friend, after a great match and conversation, Jojo continued to conquer the peaks!!!")
sleep(1)

print("Jojo reached the mountain, time to choose one of the mountain tops!\n"
          "1) Mount 1\n"
          "2) Mount 2\n")
sleep(1)
print("*It is recommended to go in turn from 1*")
while input() == "1":
    print("Unfortunately, there is nothing on this mountain, you should choose another one :(")
    sleep(1)
if input() == "2":
    print("Here is the altar itself, Jojo Places all the stones and before him appears his last enemy, Arsen")
    sleep(1)
    print("During the battle, Jojo found out that Arsen is the philosopher's stone, his soul consists of three stones, one of them is in Jojo's clothes, and the other one he uses, the third pebble is used by Arsen, who will be able to take possession of this power?")
    sleep(1)

hero1.effect(hero10)
sleep(1)
hero10.super(hero1)
sleep(1)
hero10.effect(hero1)
sleep(1)
hero1.effect(hero10)
sleep(1)
hero1.fight(hero10)
sleep(1)
print("Arsen did not stand up in the fight against Jojo, but Arsen knew from the very beginning that he had many chances, so at the end of the fight he was able to take out the stone from Jojo!!!")
sleep(1)
print("Arsen is already near the stone, but Jojo has the choice to finish off the arsenic with magic or grab the stone with his own hands "
      "1) Use magic "
      "2) Try to catch a stone")

while input() == "1":
    print("Jojo used magic, but Arsen was able to parry the blow, he reached the stone, getting energy he used his special move, which killed Jojo!!!")
    sleep(1)
    print("You beat the game with a bad ending")
if input() == "2":
    print("Jojo tried to get close to the stone himself, but not in vain, nearby he was able to parry a weak blow from Arsena, after which death overtook the latter...")
    sleep(1)

print("You passed the game to the good end!!!")