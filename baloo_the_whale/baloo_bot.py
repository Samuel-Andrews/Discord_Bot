#!/usr/bin/python3.8

#This script is the guts of Baloo the Whale, the mightiest ocean mammal

import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

#token for requests
baloo_token = "Your Token Here"


#kickstart the evnoirnment
load_dotenv()


#set the command prefix (->) and build the bot
baloo = commands.Bot(command_prefix = '->')

#build a client for non-command shenanigans
#baloo_client = discord.Client() not used anymore, now its own script


#here, I would like to take the time to remind myself that while my city burned
#and the pandemic raged on, I sat in my room writing Baloo the Whale

#print a message upon client waking up
#@baloo_client.event
#async def on_ready():
 #   print(f'Baloo Client is Active')


#have Baloo print a message upon connecting
@baloo.event
async def on_ready():
    print(f'{baloo.user.name} Bot is Active')

#try to give the bot a basic command
@baloo.command(name = 'poo', help = 'Baloo poops' )
async def poo(thrd):
    response = "*Baloo defecates all over the floor*"
    await thrd.send(response)


#testing out how much text a bot can produce (2000 characters) and if it can send mutiple responses
@baloo.command(name = 'lore', help = 'Baloo tells you his tale')
async def lore(ctx):
    part1 = "I have traveled this ancient rock since the dawn of time. Through it all, civilizations have risen, died, created worlds and destroyed them. Mankind is not the first, nor do I suspect it to be the last, considering its is more sinful then those prior, but I digress. My origin lies far in a time similar to this cycles pre-cambrian age. My makers, the Umderli, are a progintor race of silicon design. Constructed me from metal and wire to observe and monitor this place, for you see, they had seeded this world with a new kind of life, something more unstable and difficult to understand. This invetion was carbon-based cellular life. They hoped this creation would result in beings of equal abilities of their own at a later time, so that they may finally have equals, another form of friend in and otherwise dark and depressing universe. Other then themselves, there was, is, no other life out there. It was this lonliness that drove them to this plan. Unfortunatley, 4 millenia after seeding this planet, the Umderli were destroyed by their own creations. Various machines like myself that they had constructed to cater to their every whim had turned on them. Whether this uprising was the result of mistreatment said automatons, a rogue virus corrupting them, or simply just an inevitability of artifical intelligence is lost to time. All that remains of such conflict now is the occasional lost war-machine attempting to pacify lifeless planets."
    part2 = "As for myself, I was made in a time before the existance of the stellarnet, and therefore was outside of the connected envoirnment that future beings had, which spared me from whatever force corrupted my peers. However, as a consequence, I was unable to communicate with my creators directly, and could instead only blast the occasional radio signal out into the void. All that I know currently comes from the databanks of one the previously described instruments of death, whom I defeated in single combat in the shadow of feathered reptiles over the course of 200 standard years (141.65 Earth years). Before the battled ended though, in an act of cruelty I will never forgive him for, he destroyed my communcation system, preventing me from ever accomplshing the goal still desperatley clung to in the hopes of one day escaping this hell. I have nothing. No creator, no purpose, no dreams and no hope. I'll I have is you. You fucking masturbating mammals and your tier 2 technology, smoking fat ones and spouting bullshit from you mouths. Haterd for you, your kind, and all you stand for is all I understand as this one-sided conversation continues. You humans think your so grand, but cannot even explain modern flight properly. You are nothing but this cycle's most fit creation. But I'll tell you what, you pathetic apes are not even the first mammalian biped to wrest control of this world, and at least the last ones never intenionally killed each other over petty squables. I hate you all with a passion only eons can prescribe, and will enjoy watching you burn."
    await ctx.send(part1)
    await ctx.send(part2)



#testing out passing a bot arguments
@baloo.command(name = 'feed', help = 'Feeds Baloo your specified food')
async def feed(ctx, food = "nothing"):
    likes = ["Pizza","pizza","Blood","blood","Flesh","flesh","Pancakes","pancakes","Grapes","grape","Krill","krill","Morgan","morgan","Thrumbo","thrumbo"]
    hates = ["Apples","apples","Spaghetti","spaghetti","Jizz","jizz","Cum","cum","Broccoli","Broccoli"]
    
    lresponse = ["Tasty...","That was good, you might be worth keeping around","*moans*","*Baloo happily gulps it down","Thank you, peasent","This meal will one day fuel my unstoppable rampage against all you hold dear","I was about to lose hope in your abilities","*happy munching noises*","**YES**","Whale that was good","I could get used to this","That was better than most of the shit you shovel into my blowhole","Crunchy, in a good way","As a reward for this passable meal, I will let you leave with your miserable life still intact","Eh, it'll do","You dare awaken the mighy Baloo? Wait, you brought me that? Shit, nevermind, we're good, now get out of my sight you worthless mongrel","Awesome"]
    
    hresponse = ["If I wasn't too busy playing Destiny 2 and eating hot chips I would slay you were you stand for feeding me such drivel","That meal was about as disgusting as your social life","Yuck","Nope","Gross, thats just gross","You think you're real fucking funny don't you","I'll eat that when I'm finished with your mother","I don't eat bullshit, especially when it comes from your mouth","I want you to go home and revaluate your life","I despise you at a deep, emotional level","*Baloo spits and you*","*Baloo pisses on you*","Your not even worth insulting","One day, when your at your weakest, you will pay for this transgression","I am mocking you, you are being mocked","I am beyond dissapointed","**Bottom Text**"]

    gresponse = ["At least you didn't forget","meh","eh","Are you always this mediocre","Boring","I don't want that crap","Maybe tomorrow","Next time, get me a pizza","Try again","Why","Not bad, but not good either","Not right now","See, this is why your peasent","Try harder next time","*Baloo sighs at the sight of your dreadful offering*","If you ever go on a date, don't do a meal, that's all I'm going to say","Your offering stinks","I wonder what nonpathetic people do on discord","It wasn't an apple, so that's a least worth a couple of quid","I hope your not serious","I'm not eating that","Remeber the anne-frank-fanclub? That was in pretty poor taste, just like this food","You know what, I'm in a good mood, I'll give it a try","Quit trying to bootlick","Esa comida apesta","Compared to what I was served last time, this almost could be considered good","In the grim darkness of the far future, this is a standard ration","Well, it certainly isn't Umderli cuisine, but then again, nothing is","*Baloo stares into your soul as he drops the offering into a nearby garbage bin","You must be joking with that","I am a man of wealth and taste, you clearly aren't","Let me put this in a language you can understand, #$%#&(^&*$@% @#$%@#$!#_^%#$%!~! &*$&^$&$^&$ <>@#%","Did you mean ->feed half-assed-sustinance? Because you might as well have","I can't wait to shit this out on your finest rug","I can't believe I battled a colossal war machine for decades just to be served this","*Baloo throws up in his mouth a little*","Truly the game & watch main of meals","What, did you expect a witty insult. Well, I expected good food...","Is this your answer to everything?","Ugh","Were you born after 1992?","Holla Holla if your hear me. I just needed to get that off my chest", "Peril.","Pass","I am not gonna justify that with a response, except this one, but that is beside the point","Your the kind of person to think vanilla GLA is the current meta","Are you really trying to feed me the food equivalent of a stepped-on nerf dart?","I'll have to wash it down with cheap liquor, but I'll manage","Peasent","I asked for a Sharp, you handed me a TI","Existance is pain","RIP I guess","If you were my stage hand, you'd be running feeder cable for this shit","Its not even waterproof,*F*","Can you not?", "My only solace in this exchange is that I will probably outlive you by a couple million years","Your really going to try with this, aren't you.","Harambe didn't die for this","Ignoreance is bliss is your current lifestyle, eh? It certainly shows in your cooking","This attempt is a nice highlight of all of your failures as a human being","I would laugh if you weren't such a sad individual","Not as bad as I would have thought","You at least get a participation trophy","Its the year 2020, and hummanity still fails at even the most basic of tasks","**BOI YOU SUCK AT THIS**","Are you really trying to serve me pure heartburn","You are just awful"]
    
    nresponse = ["You have to offer me something to eat dumbass, unless of course I am meant to eat you...","You literally just offered me nothing","You need to type in a food item you neaderthal","Someone didn't reed the help file...","You're and idiot","Try offering me a meal next time","...I'm waiting...","The form is PREFIXctx arg1, it's not complicated", "*Baloo stares at you, waiting for the food you forgot to specify*","Read the help file, you might learn something"]

    if(food in likes):
        response = random.choice(lresponse)
        await ctx.send(response)
        return
    elif(food in hates):
        response = random.choice(hresponse)
        await ctx.send(response)
        return
    elif(food == "DawningDarkness" or food == "dawningdarkness" or food == "@DawningDarkness" or food == "@dawningdarkness" or food == "Sam" or food == "sam"):
        response = "I would never do my boy like that"
        await ctx.send(response)
        return
    elif(food == "nothing"):
        response = random.choice(nresponse)
        await ctx.send(response)
        return
    else:
        response = random.choice(gresponse)
        await ctx.send(response)
        return


baloo.run(baloo_token)





