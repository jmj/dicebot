#!/usr/bin/python

from jabberbot import JabberBot, botcmd
import random

class JBot(JabberBot):
    @botcmd
    def roll(self, msg, args):
        '''Causes the bor to roll dice:
        roll 6d6
        as an example'''
        (ndice, nbsides) = args.upper().split('D')

        tmp = nbsides.split('+')
        nsides = tmp[0]
        if len(tmp) == 1:
            bonus = 0
        elif len(tmp) == 2:
            bonus = tmp[1]
        else:
            return "I'm confised"

        if ndice == '':
            ndice = 1


        try:
            numdice = int(ndice)
        except:
            numdice = 0
        try:
            numsides = int(nsides)
        except:
            numdice = -1
        try:
            bonus = int(bonus)
        except:
            return "I'm confused again  "

        if numdice <= 0:
            return 'Hu?? ', tmp

        #rnd = random.SystemRandom()
        rnd = random.Random()

        x = 0
        r = 'rolls: '
        for i in range(0,numdice):
            s = rnd.randint(1,numsides)
            x = x + s
            r = '%s %s' % (r,s)

        return '%s\nTotal: %s' % (r, x+bonus)




if __name__ == '__main__':
    bot = JBot('jbot@letifer.org', 'sl1me2')
    bot.serve_forever()
