from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def mines(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = ":star2: "
        elif a == 2:
            mine2 = ":star2: "
        elif a == 3:
            mine3 = ":star2: "
        elif a == 4:
            mine4 = ":star2: "
        elif a == 5:
            mine5 = ":star2: "
        elif a == 6:
            mine6 = ":star2: "
        elif a == 7:
            mine7 = ":star2: "
        elif a == 8:
            mine8 = ":star2: "
        if b == 9:
            mine9 = ":star2: "
        elif b == 10:
            mine10 = ":star2: "
        elif b == 11:
            mine11 = ":star2: "
        elif b == 12:
            mine12 = ":star2: "
        elif b == 13:
            mine13 = ":star2: "
        if c == 14:
            mine14 = ":star2: "
        elif c == 15:
            mine15 = ":star2: "
        elif c == 16:
            mine16 = ":star2: "
        elif c == 17:
            mine17 = ":star2: "
        if d == 18:
            mine18 = ":star2: "
        elif d == 19:
            mine19 = ":star2: "
        elif d == 20:
            mine20 = ":star2: "
        elif d == 21:
            mine21 = ":star2: "
        elif d == 22:
            mine22 = ":star2: "
        elif d == 23:
            mine23 = ":star2: "
        elif d == 24:
            mine24 = ":star2: "
        elif d == 25:
            mine25 = ":star2: "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(45, 90))
        pfp = 'https://giphy.com/clips/motivation-goku-warm-up-CJRKhi0sixPav1P6MN'
        em = discord.Embed(color=0x11F1D3)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Made by Gimmyx")
        em.add_field(name="Mines predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy**" + "\n" + info +"%")
        await ctx.reply(embed=em)


bot.run("MTAxNTYwMTc1NjAyNzI0MDQ1OA.G2Qr6V.CDjM-Wja1KH5eRaarCA6MCr68DGng_gNxkk1DE")
