import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

bot = commands.Bot(command_prefix='*')

global requests
requests = 0

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def stats(ctx, a: str):
    try:
        url = 'https://fortnitestats.net/stats/'+a
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "lxml")
        
        overall_stats = soup.find_all('h3')
        counter = 0
        for value in overall_stats:
            if counter < 6:
                overall_stats[counter] = str(overall_stats[counter]).replace('<h3>', '')
                overall_stats[counter] = str(overall_stats[counter]).replace('</h3>', '')
            counter = counter + 1      
        specific_stats = soup.find_all('p')
        counter = 7
        while counter > 6 and counter < 28:
            specific_stats[counter] = (str(specific_stats[counter]).replace('<p>', '').replace('</p>', '').replace('rounds played', ''))
            counter = counter + 1
        
        embed = discord.Embed(title="Overall Stats", description="Overall Fornite stats of "+a, color=0xeee657)
        embed.add_field(name='--------------------------------------', value="**Total Kills:** "+overall_stats[0])
        embed.add_field(name='--------------------------------------', value="**KDR:** "+overall_stats[1])
        embed.add_field(name='--------------------------------------', value="**Win/Loss Rate:** "+overall_stats[2])
        embed.add_field(name='--------------------------------------', value="**Total Wins:** "+overall_stats[3])
        embed.add_field(name='--------------------------------------', value="**Total Matches:** "+overall_stats[4])
        embed.add_field(name='--------------------------------------', value="**Total Hours:** "+overall_stats[5])
        
        embed0 = discord.Embed(title="Solo Stats", description="Solo stats of "+a, color=0xeee657)
        embed0.add_field(name='--------------------------------------', value="**Rounds played:** "+specific_stats[7])
        embed0.add_field(name='--------------------------------------', value="**Total Wins:** "+specific_stats[8])
        embed0.add_field(name='--------------------------------------', value="**Total Kills:** "+specific_stats[9])
        embed0.add_field(name='--------------------------------------', value="**KDR:** "+specific_stats[10])
        embed0.add_field(name='--------------------------------------', value="**Top 5:** "+specific_stats[11])
        embed0.add_field(name='--------------------------------------', value="**Top 10:** "+specific_stats[12])
        embed0.add_field(name='--------------------------------------', value="**Top 25:** "+specific_stats[13])
        
        embed1 = discord.Embed(title="Duo Stats", description="Duo stats of "+a, color=0xeee657)
        embed1.add_field(name='--------------------------------------', value="**Rounds played:** "+specific_stats[14])
        embed1.add_field(name='--------------------------------------', value="**Total Wins:** "+specific_stats[15])
        embed1.add_field(name='--------------------------------------', value="**Total Kills:** "+specific_stats[16])
        embed1.add_field(name='--------------------------------------', value="**KDR:** "+specific_stats[17])
        embed1.add_field(name='--------------------------------------', value="**Top 5:** "+specific_stats[18])
        embed1.add_field(name='--------------------------------------', value="**Top 10:** "+specific_stats[19])
        embed1.add_field(name='--------------------------------------', value="**Top 25:** "+specific_stats[20])
        
        embed2 = discord.Embed(title="Squad Stats", description="Squad stats of "+a, color=0xeee657)
        embed2.add_field(name='--------------------------------------', value="**Rounds played:** "+specific_stats[21])
        embed2.add_field(name='--------------------------------------', value="**Total Wins:** "+specific_stats[22])
        embed2.add_field(name='--------------------------------------', value="**Total Kills:** "+specific_stats[23])
        embed2.add_field(name='--------------------------------------', value="**KDR:** "+specific_stats[24])
        embed2.add_field(name='--------------------------------------', value="**Top 5:** "+specific_stats[25])
        embed2.add_field(name='--------------------------------------', value="**Top 10:** "+specific_stats[26])
        embed2.add_field(name='--------------------------------------', value="**Top 25:** "+specific_stats[27])
        
        await ctx.send(embed=embed)
        await ctx.send(embed=embed0)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
        
    except:       
        await ctx.send('This user was not found!')
        
    global requests
    requests += 1
    print("Total times ran: "+str(requests)+". This time: *STATS")    

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="LarsBot", description="A bot made by justLars7D1!", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="justLars7D1#3134")
                    
    #coded
    embed.add_field(name="Programmed in", value="Python")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=416951424157745154&permissions=0&redirect_uri=https%3A%2F%2Fwww.justLars7D1.com%2FMEET&scope=bot")

    await ctx.send(embed=embed)
    
    global requests
    requests += 1
    print("Total times ran: "+str(requests)+". This time: *INFO")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="LarsBot", description="A bot made by justLars7D1. List of commands are:", color=0xeee657)

    embed.add_field(name="*stats X", value="Gives the Fortnite stats of player **X**", inline=False)
    embed.add_field(name="*info", value="Gives info about this bot", inline=False)
    embed.add_field(name="*help", value="Gives this message", inline=False)
    
    global requests
    requests += 1
    print("Total times ran: "+str(requests)+". This time: *HELP")    

    await ctx.send(embed=embed)

bot.run('NDE2OTUxNDI0MTU3NzQ1MTU0.DXMGmg.mo_LtXdnfko2VR0GKB3I2iF5SgY')
