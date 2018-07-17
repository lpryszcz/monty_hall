#!/usr/bin/env python

import random

def monty_hall(change=True, n=100000, sample=range(3)):
    """Compute success rate for Monty Hall problem"""
    success = 0
    for x in xrange(n):
        prize = random.choice(sample)
        player = random.choice(sample)
        opened = random.choice(list(set(sample).difference([prize, player])))
        if change:
            player = random.choice(list(set(sample).difference([opened, player])))

        if player == prize:
            success += 1
        
    rate = 1.*success/n
    print("Success %s out of %s when change=%s. Success rate: %.5f"%(success, n, change, rate))
    return rate

if __name__=="__main__":
    monty_hall(change=False)
    monty_hall(change=True)
