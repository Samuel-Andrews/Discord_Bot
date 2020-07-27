#!/usr/bin/python3.8

#   !CLIENT!


#This script is the guts of Baloo the Whale, the mightiest ocean mammal


#important IDs

#me "DawningDarkness" = 318797953160445963

#test adv chat = 719313108182630430

#real adv chat = 562410209570717718




import random
import discord
from discord.ext import commands
from dotenv import load_dotenv


#token for requests
baloo_token = "Your Token Here"


#kickstart the envoirnment
load_dotenv()



#build the client
baloo_client = discord.Client()




#print a message upon client waking up
@baloo_client.event
async def on_ready():
    await baloo_client.change_presence(status=discord.Status.idle, activity = discord.Game('You like a damn fiddle'))
    print(f'Baloo Client is Active')




#if someone types a message in into either the test adv chat or the actual (order is the same), it will react with an egg
@baloo_client.event
async def on_message(text):
   
    #never reacts to its own messages
    if text.author == baloo_client.user:
        return

    #if someone types in "baloo", reacts negatvely
    if 'baloo' in text.content:
        await text.channel.send('Capitalize my name, peasent')

    #if someone asks if Baloo is a player
    if 'Baloo, are you a player?' in text.content:
        await text.channel.send("I'm not a player, I just fuck a lot")
    
    #if someone types in a quote in daily verse, they get an amen
    if((text.channel.id == 719700247487447100 or text.channel.id == 562409848902254612) and "\"" in text.content):
        await text.channel.send("Amen")
    
    #if a pic is posted in nsfw, Baloo might say something
    #this if statement could be cleaned up, but it helped me learn python syntax
    if((text.channel.id == 719702856244133958 or text.channel.id == 562410692028792843) and (text.content.endswith(".jpg") or text.content.endswith(".png") or text.content.endswith(".jpeg") or ".png" in text.attachments[0].url or ".jpg" in text.attachments[0].url or ".jpeg" in text.attachments[0].url)):
        
        reactroll = random.randint(0,2)

        if(reactroll == 2):
            
            nsfwcom = ["That's just gross","You all continue to dissapoint me","4/10","This is why DawningDarkness stay out of this shithole", "Grade B fap material","I'd summon it","My kind of style", "This reminds me of the stuff the Umderli use to browse", "Poor thing", "*Baloo Vomits*", "I was having a perfectly good day", "My robo-cock just rusted", "I miss the supercrown gals", "aight, imma head out", "This is what were fighting for", "So, this is what hell is", "Mankind has really outdone themselves", "Is this lore?", "I hate this", "Is this supposed to be porn?", "We all deserve better", "Is that Mark Zuckerberg?", "Trash", "*Baloo screams*", "*Baloo lets out a heavy sigh*", "My eyes will never unsee that", "Actually, thats not that bad", "I think its time for a revolution", "Imagine fapping to this","Predictable","I see you are a man of culture", "Reminds me of that time in Nicaragua back in '78", "It's not coke on tits, but it'll do", "*Whale noises", "That right there is a total mood", "Why?","cOmeDy","We will all pay for these crimes one day","You make me wanna cry", "This has nothing to due with the porn, but have you guys ever tried thrumbo? It'll change your life", "What a bunch of Bitches", "Warms the mechanical heart", "You cleary lack self-respect", "I'm speechless", "This is why I poop", "01100100 01101001 01100101", "**GOOD**","I now have sympathy for the devil", "I lost hope I didn't even know I still had", "oof", "How could you?", "Truly, I now reside in hell", "The embodiment of sin", "I wish that was posted ironically, but i know deep down it wasn't", "This some kind of commentary of the higher Arts", "This one is going into my homework folder","I hope this doesn't get is own category one day...", "Some people just want to watch the world burn, and I agree", "Check please"]
            response = random.choice(nsfwcom)
            await text.channel.send(response)




    #Everyone in both test and real adv. chats gets an egg
    if(text.channel.id == 719313108182630430 or text.channel.id == 562410209570717718):
        await text.add_reaction("🥚")
    
    #I am always given an egg
    if((text.author.id == 318797953160445963) and (text.channel.id != 719313108182630430 or text.channel.id != 562410209570717718)):
        await text.add_reaction("🥚")


baloo_client.run(baloo_token)






