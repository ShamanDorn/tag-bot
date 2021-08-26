from discord.ext.commands import Cog
from discord.ext.commands import command

class Emoticon(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="bunny", pass_context=True)
    async def bunny(self, ctx, arg):
        #if len(arg) == 1:
        await ctx.send(f"<:nothing:848524427037769728>/|  /|\n  ( => v <)=\no(       >{arg}>")
        #else:
            #await ctx.send("waaa only one emoji pwease")

    @command(name="vibe", pass_context=True)
    async def vibe(self, ctx, arg):
        await ctx.send(f"{arg}(๑ᴖ◡ᴖ๑){arg}")

    @command(name="fries", pass_context=True)
    async def fries(self, ctx, arg):
        await ctx.send("`{\_/}`\n( • - •)\n/ >  🍟  Want my fries?")
        await ctx.send("`{\_/}`\n( • - •)\n🍟 < \  Get your own fries!")
        await ctx.send("`{\_/}`\n( • - •)\n" + f"/ > {arg}  But you can have this!")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("emoticon")

def setup(bot):
    bot.add_cog(Emoticon(bot))