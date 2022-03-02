#!/usr/bin/env python
"""
    ECE-203 Lab Assignment 10

    Author: James A. Shackleford <shack@drexel.edu>

    In this assignment you have been given a very simple
    framework that pits an army of Clones against an army
    of Robots.  It is your job to create Clone and Robot
    classes that are compatible with the framework.

    The army of Robots will attack first.  Each Robot will
    shoot randomly at Clones (up to 5 times) until it hits
    one for damage.  Once all Robots have attempted to
    attack, it will be the Clones' turn.

    The army of Clones will attack second.  Each Clone will
    shoot randomly at Robots (up to 5 times) until it hits
    one for damage.  After a Clone hits a Robot, there is a
    0.3% chance it will issue Order 66.  This will cause all
    Clones to shoot themselves instead of their randomly
    chosen targets when they pull the trigger on their
    blasters.  Once all Clones have attempted to attack,
    it will again be the Robots' turn.

    Once either all Clones are dead or all Robots are dead,
    the simulation will end.
"""

import os
import time
from random import random as R
from random import choice as getRandom



######################################################################
import random

class Robot:
    def __init__(self, hitpoints, damage):
        self._hitpoints = hitpoints
        self._damage = damage
        self._dead = False

    def takeDamage(self, damagetaken):
        self._hitpoints -= damagetaken
        if self._hitpoints<= 0:
            self._dead = True

    def shoot(self, target):
        if not self._dead:
            target.takeDamage(self._damage)

    def dead(self):
        return self._dead

    def hitpoints(self):
        if self._dead:
            return str('DEAD')
        else:
            return self._hitpoints


class Clone:

    _order66 = False

    def __init__(self, hitpoints, damage):
        self._hitpoints = hitpoints
        self._damage = damage
        self._dead = False

    def takeDamage(self, damagetaken):
        self._hitpoints -= damagetaken
        if self._hitpoints <= 0:
            self._dead = True

    def shoot(self, target):
        if not self._dead:
            self._shoot(target)
        if not Clone._order66:
            self.issueOrder66()

    def dead(self):
        return self._dead

    def hitpoints(self):
        if self._dead:
            return str('DEAD')
        else:
            return self._hitpoints

    @staticmethod
    def issueOrder66():
        x = random.randint(1, 1000)
        if x <= 3:
            Clone._order66 = True

    def _shoot(self, target):
        if Clone._order66:
            self.takeDamage(self._damage)
        else:
            target.takeDamage(self._damage)



######################################################################



def printBattleStatus(cloneArmy, robotArmy):
    """
        ACCEPTS:
            cloneArmy - a list of Clone objects
            robotArmy - a list of Robot objects
        RETURNS:
            Nothing

        Clears the screen and prints the hitpoints of all the
        clone soldiers on the left and all the robot soldiers
        on the right.  Example output:

            Clones         Robots
            -----------------------
            [   40 ]       [ DEAD ]
            [   25 ]       [ DEAD ]
            [   20 ]       [   20 ]
            [ DEAD ]       [   50 ]
            [   35 ]       [ DEAD ]
            [   20 ]       [   80 ]
            [    5 ]       [   40 ]
            [   45 ]       [ DEAD ]
            [   40 ]       [ DEAD ]
            [   15 ]       [   20 ]
    """

    os.system('clear')
    if Clone._order66 is True:
        print '   [ !! ORDER 66 !! ]'

    print ' Clones         Robots'
    print '-----------------------'
    for clone, robot in zip(cloneArmy, robotArmy):
        print '[ %s ]       [ %s ]' % (clone.hitpoints(), robot.hitpoints())

    time.sleep(1)


def allDead(army):
    """
        ACCEPTS:
            army - a list of either Robot or Clone objects

        RETURNS:
            True  <-- if all objects in army are dead
            False <-- if at least 1 object in army is not dead


        This function simply accepts a list of either Robot or
        Clone objects and returns True if all the soldiers are
        dead; otherwise it returns False
    """

    for soldier in army:
        if soldier.dead() is False:
            return False

    return True


def launchAttack(attackers, victims):
    """
        ACCEPTS:
            attackers - a list of either Robot or Clone objects
            victims - a list of either Robot or Clone objects

        RETURNS:
            Nothing

        This function iterates through attackers and invokes the
        shoot(victim) method for each attacker.  The victim is a
        randomly selected object from the victims list.  If a victim
        is already dead, the attacker will attempt randomly choose
        another victim.  If the attacker can't find an alive victim
        after 5 tries, it gives up and doesn't attack anybody.
    """

    for attacker in attackers:
        # dead attackers can't attack
        if attacker.dead():
            continue

        # target a victim that is not dead
        # try up to 5 times
        tries = 0
        victim = getRandom(victims)
        while victim.dead():
            victim = getRandom(victims)
            tries += 1
            if tries > 4:
                return

        attacker.shoot(victim)


if __name__ == '__main__':
    cloneArmy = []
    robotArmy = []

    # Create two armies, each with 10 soldiers
    #   Clones have 100 HP and do 10 damage
    #   Robots have 180 HP and do  5 damage
    for _ in xrange(10):
        cloneArmy.append(Clone(100, 10))
        robotArmy.append(Robot(180, 5))

    # Kick off the main event loop
    printBattleStatus(cloneArmy, robotArmy)
    while (not allDead(cloneArmy) and (not allDead(robotArmy))):

        # robot army attacks clone army 1st
        launchAttack(robotArmy, cloneArmy)

        # clone army attacks robot army 2nd
        launchAttack(cloneArmy, robotArmy)

        printBattleStatus(cloneArmy, robotArmy)
