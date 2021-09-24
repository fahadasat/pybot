#Matty bot
#create reminders, add calender
import discord
from discord.ext import commands
import random
import asyncio
import datetime
import requests
import calendar

client = discord.Client()
bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(game=discord.Game(name='at the Oviatt | ~botinfo'))


@bot.command(pass_context=True)
async def botinfo():
    print("botinfo")
    embed = discord.Embed(title="Bot Name", description="MattyBot", color=0x8942f4)
    embed.set_footer(text="To serve the Matadors!")
    embed.set_author(name='Bot Information', icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url="https://s1.ticketm.net/tm/en-us/dam/a/4ff/403d3d47-7f19-495a-af68-f271bcae64ff_246081_CUSTOM.jpg")
    embed.add_field(name="Main Commands:", value="~say 'word' -- Make the bot say something! "
                                           "\n ~Matty "
                                           "\n ~Once a Matador -- Always a Matador! "
                                           "\n ~Who is a Matador -- Who is a Matador?"
                                           "\n ~rateme -- Have Matty give you a rating"
                                           "\n ~calendar -- All calendar commands "
                                           "\n ~map -- Provides you with the CSUN map"
                                           "\n ~water -- Provides you with water refill locations", inline=False)
    embed.add_field(name="Created On", value=bot.user.created_at, inline=False)
    await bot.say(embed=embed)


@bot.event
async def on_message(message):

    if message.author.id != bot.user.id:
        if message.author.id == '330011881341452288':
         #   await bot.delete_message(message)
            print('deleted')
        if message.content == "~Once a Matador":
            await bot.send_message(message.channel, "Always a Matador!")
        if message.content == "~Who is a Matador":
            await bot.send_file(message.channel, "./Matty-YOU.jpg")
        if message.content == "~Matty":
            await bot.send_file(message.channel, "./whomatty.jpg")
        if message.content == "~map":
            await bot.send_file(message.channel, "./map.jpg")
        if message.content == "~water":
            await bot.send_file(message.channel, "./water.jpg")
        if message.content == ":matathonk_extreme:":
            await bot.send_message(message.channel, ":mmm:")
        if "good morning" in message.content.lower():
            now = datetime.datetime.now()
            if 5 <= now.hour < 10:
                await bot.send_message(message.channel, "**Morning!**")
        if "good night" in message.content.lower():
            now = datetime.datetime.now()
            if 21 <= now.hour <= 23 or 0 <= now.hour <= 3:
                await bot.send_message(message.channel, "**good night!**")
        if "cya" in message.content.lower():
            await bot.send_message(message.channel, "cya " + message.author.name)
        if "thank you" in message.content.lower():
            await bot.send_message(message.channel, "no problem " + message.author.name)
        if "gracias" in message.content.lower():
            await bot.send_message(message.channel, "denada " + message.author.name)
        if "good luck" in message.content.lower():
            await bot.send_message(message.channel, "yeah man good luck")
        await bot.process_commands(message)


@bot.command(pass_context=True)
async def say(ctx):
    print("say")
    await bot.say(ctx)


@bot.command(pass_context=True)
async def rateme(ctx):
    print("rateme")
    await bot.say("**"+ctx.message.author.name + " is a " + str(randInt(10)) + "/10!**")


@bot.command(pass_context=True)
async def calendar():
    print("calendar")
    embed = discord.Embed(title="Calendar:", description=None, color=0x5c42f4)
    embed.add_field(name="~upcoming 10", value="• all events happening from today to desired date", inline=False)
    embed.add_field(name="~day", value="• all events happening today", inline=False)
    embed.set_footer(text="Shoutout to omioni for helping")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def upcoming(ctx):
    print("upcoming")
    if int(ctx) == 1:
        await bot.say("**:anger: Use ~day for todays events!**")
    elif int(ctx) < 1:
        await bot.say("Invalid input")
    elif int(ctx) > 4:
        await bot.say("Looking too far into the future my man")
    else:
        await bot.say("Give me a while to load it all up...")
        now = datetime.datetime.now()
        day = now.day
        ct = 0
        while (ct != int(ctx)):
            await bot.say(embed=scrapetogether(day, now.month, now.year, 1))
            ct+=1
            day+=1
        print (done)


@bot.command(pass_context=True)
async def test():
    print("test")


@bot.command(pass_context=True)
async def day():
    print("day")
    # await bot.say("Give me a while to load it all up...")
    now = datetime.datetime.now()
    await bot.say(embed = scrapetogether(now.day, now.month, now.year, 1))
    # printcal(now)


# async def printcal (now):
#     await bot.say(embed=scrapetogether(now.day, now.month, now.year, 1))



def scrapetogether (day, month, year, future):
    title = ""
    if future > 1:
        title = str(day) + " - " + datefinal(day, future, year, month)
    embed = discord.Embed(title=title, description=None, color=0x5c42f4)
    ct = 0
    while ct != future:
        scrapname = scrapename(day, month, year)
        scrapstart = scrapestart(day, month, year)
        scrapend = scrapeend(day, month, year)

        # print(len(scrapname))
        # print(len(scrapstart))
        # print(len(scrapend))
        #
        # print(scrapname)
        # print(scrapstart)
        # print(scrapend)

        # if len(scrapname) != len(scrapstart):
        #     scrapstart.pop(0)
        #     scrapend.pop(0)
        # if len(scrapname) != len(scrapend):
        #     scrapend.pop(0)

        date = (weekdate(year, month, day) + " " + (monthdate(month)) + " " + str(day))
        happening = ""
        if len(scrapname) == 0:
            happening = "• Nothing :("
        else:
            for index, item in enumerate(scrapname):
                    happening = happening + "• " + scrapname[index].strip() + ": "
                    try:
                        happening = happening + scrapstart[index].strip() + " to "
                    except IndexError:
                        print("no start")
                    try:
                        happening = happening + scrapend[index].strip() + "\n"
                    except IndexError:
                        happening = happening + "Whenever Event Finishes" + "\n"
                        print("no end")
                # happening = "".join(["• " + (a) + ": " + b.strip() + " - " + c + "\n" for a, b, c in zip(scrapname, scrapstart, scrapend)])
        # print (happening)

        embed.add_field(name=date, value=happening, inline=False)
        if day == calendar.monthrange(year, month)[1] and month != 12:
            day = 1
            month += 1
        elif day == calendar.monthrange(year, month)[1] and month == 12:
            day = 1
            month = 1
            year += 1
        else:
            day += 1
        ct += 1

    return embed


def scrapename(day, month, year):
    usu = "https://www.csun.edu/calendar-events/day/9321/" + str(year) + "-" + str(month) + "-" + str(day)
    associatedstudents = "https://www.csun.edu/calendar-events/day/9316/" + str(year) + "-" + str(month) + "-" + str(day)
    university = "https://www.csun.edu/calendar?month=" + str(year) + "-" + str(month) + "-" + str(day)
    r = requests.get(usu)
    # r1 = requests.get(associatedstudents)
    # r2 = requests.get(university)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    # soup1 = BeautifulSoup(r1.text, 'html.parser')
    # soup2 = BeautifulSoup(r2.text, 'html.parser')

    usunames = soup.find_all('span', attrs={'class': 'views-field views-field-title'})
    # asnames = soup1.find_all('span', attrs={'class': 'views-field views-field-title'})
    # uninames = soup2.find_all('h2', attrs={'class': 'node--title node-title'})

    usunamed = []
    for usuname in usunames:
        usuname = usuname.find('a').text[0:]
        usunamed.append(usuname)
    # asnamed = []
    # for asname in asnames:
    #     asname = asname.find('a').text[0:]
    #     asnamed.append(asname)
    # uninamed = []
    # for uniname in uninames:
    #     uniname = uniname.find('a').text[0:]
    #     uninamed.append(uniname)
    #
    # uninamed.pop(0)
    # print(uninamed)

    names = usunamed #+ asnamed #+ uninamed
    return names


def scrapestart(day, month, year):
    usu = "https://www.csun.edu/calendar-events/day/9321/" + str(year) + "-" + str(month) + "-" + str(day)
    associatedstudents = "https://www.csun.edu/calendar-events/day/9316/" + str(year) + "-" + str(month) + "-" + str(day)
    university = "https://www.csun.edu/calendar?month=" + str(year) + "-" + str(month) + "-" + str(day)
    r = requests.get(usu)
    # r1 = requests.get(associatedstudents)
    # r2 = requests.get(university)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    # soup1 = BeautifulSoup(r1.text, 'html.parser')
    # soup2 = BeautifulSoup(r2.text, 'html.parser')

    usustarts = soup.find_all('span', attrs={'class': 'date-display-start'})
    # asstarts = soup1.find_all('span', attrs={'class': 'date-display-start'})
    # unistarts1 = soup2.find_all('span', attrs={'class': 'date-display-start'})
    # unistarts2 = soup2.find_all('span', attrs={'class': 'date-display-single'})

    usustarted = []
    for usustart in usustarts:
        usustart = usustart.contents[0]
        usustarted.append(usustart)
    # asstarted = []
    # for asstart in asstarts:
    #     asstart = asstart.contents[0]
    #     asstarted.append(asstart)
    # unistarted1 = []
    # for unistart in unistarts1:
    #     unistart = unistart.contents[0]
    #     if unistart not in unistarted1:
    #         unistarted1.append(unistart)
    # unistarted2 = []
    # for unistart in unistarts2:
    #     unistart = unistart.contents[0]
    #     if unistart not in unistarted1:
    #         unistarted2.append(unistart)
    # print(unistarted1)
    # print(unistarted2)
    # unistarted2.pop(0)
    # print(unistarted2)
    # print(stringindex(unistarted1, "-"))
    # for index, item in enumerate(unistarted2):
    #     if "pm" in unistarted2[index]:
    #         print("in")
    #     elif "am" in unistarted2[index]:
    #         print("in")
    #     else:
    #         unistarted2[index] = unistarted2[index] + unistarted1[stringindex(unistarted1, "-")]
    #         unistarted1.pop(stringindex(unistarted1, "-"))

    started = usustarted# + asstarted #+ unistarted1 + unistarted2
    # print(len(started))
    # print (unistarted1 + unistarted2)
    return started


def stringindex(the_list, substring):
    for i, s in enumerate(the_list):
        if substring not in s:
            return i


def scrapeend(day, month, year):
    usu = "https://www.csun.edu/calendar-events/day/9321/" + str(year) + "-" + str(month) + "-" + str(day)
    # associatedstudents = "https://www.csun.edu/calendar-events/day/9316/" + str(year) + "-" + str(month) + "-" + str(day)
    # university = "https://www.csun.edu/calendar?month=" + str(year) + "-" + str(month) + "-" + str(day)

    r = requests.get(usu)
    # r1 = requests.get(associatedstudents)
    # r2 = requests.get(university)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    # soup1 = BeautifulSoup(r1.text, 'html.parser')
    # soup2 = BeautifulSoup(r2.text, 'html.parser')

    usuends = soup.find_all('span', attrs={'class': 'date-display-end'})
    # asends = soup1.find_all('span', attrs={'class': 'date-display-end'})
    # uniends = soup2.find_all('span', attrs={'class': 'date-display-end'})

    usuended = []
    for usuend in usuends:
        usuend = usuend.contents[0]
        usuended.append(usuend)
    # asended = []
    # for asend in asends:
    #     asend = asend.contents[0]
    #     asended.append(asend)
    # uniended = []
    # for uniend in uniends:
    #     uniend = uniend.contents[0]
    #     uniended.append(uniend)
    ended = usuended #+ asended #+ uniended
    # print(uniended)
    return ended


def weekdate(year, month, day):
    weekday = datetime.date(year, month, day).weekday()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[weekday]


def monthdate(month):
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
    return months[month-1]


def randInt(x):
    if x > 0:
        rand = random.randint(0, x)
    elif x == 0:
        rand = 0
    return rand

def datefinal(day, future, year, month):
    ct = 1
    while ct != future:
        if day == calendar.monthrange(year, month)[1]:
            day = 1
        else:
            day += 1
        ct +=1
    return str(day)



bot.run("")
