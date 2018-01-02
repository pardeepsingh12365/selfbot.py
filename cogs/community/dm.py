
Free TNT - Today at 6:14 PM
Ye
Stingy - Today at 6:14 PM
Ok you help them
Free TNT - Today at 6:15 PM
the versions stuff is important, u wanna change so the old cog work? Then ur breaking ur whole selfbot cuz it uses the new version
Stingy - Today at 6:16 PM
Maybe you can just delete the cog :thinkblob:
I mean not use it
PK - Today at 6:16 PM
oh so i cant do it
??
Stingy - Today at 6:17 PM
Well it's doable but it won't be that easy
It's like this
You have a file that's written in old code
Rest of files are in new code
Version is currently set to new code
Best solution is to rewrite that one file to new version
Free TNT - Today at 6:18 PM
Lol
This ain't selfbot server anymore tho. A lot got banned so barely anyone is working on it
PK - Today at 6:19 PM
can anyone convert the massdm code with specific version of discord.py.
Stingy - Today at 6:19 PM
Is it Python or?
Free TNT - Today at 6:19 PM
I don't do illegal stuff :LOL:
PK - Today at 6:20 PM
ya its on python
Stingy - Today at 6:20 PM
Send me the file
I'll try
:thinkblob:
PK - Today at 6:20 PM
ok bro
Free TNT - Today at 6:20 PM
...
Stingy - Today at 6:20 PM
@Free TNT Relax
SharpBit - Today at 6:20 PM
computer.vbs
Stingy - Today at 6:20 PM
It's bad for the person who uses it
@SharpBit xd
V I S U A L    B A S I C   T H E    O L D   B O I
Free TNT - Today at 6:21 PM
Lol
:Bleach:
PK - Today at 6:21 PM
import discord
from typing import List

from discord.ext import commands


class MassDM:

    """Send a direct message to all members of the specified Role."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def _member_has_role(self, member: discord.Member, role: discord.Role):
        return role in member.roles

    def _get_users_with_role(self, server: discord.Server,
                             role: discord.Role) -> List[discord.User]:
        roled = []
        for member in server.members:
            if self._member_has_role(member, role):
                roled.append(member)
        return roled

    @commands.command(no_pm=True, pass_context=True, name="massdm",
                      aliases=["mdm"])
    async def _mdm(self, ctx: commands.Context,
                   role: discord.Role, *, message: str):
        """Sends a DM to all Members with the given Role.
        Allows for the following customizations:
        {0} is the member being messaged.
        {1} is the role they are being message through.
        {2} is the person sending the message.
        """

        server = ctx.message.server
        sender = ctx.message.author

        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass

        dm_these = self._get_users_with_role(server, role)

        for user in dm_these:
            try:
                await self.bot.send_message(user,
                                            message.format(user, role, sender))
            except (discord.Forbidden, discord.HTTPException):
                continue


def setup(bot: commands.Bot):
    bot.add_cog(MassDM(bot))
Stingy - Today at 6:21 PM
I want to drink that :yum:
Lemme see :thinkblob:
PK - Today at 6:21 PM
k
Stingy - Today at 6:21 PM
So I should modify whole cog?
Or just a command?
PK - Today at 6:22 PM
idk:sweat_smile:
Free TNT - Today at 6:23 PM
Whole cog
Lol
Rewrite is like almost a new lib
PK - Today at 6:28 PM
thats was erorr
AttributeError: module 'discord' has no attribute 'Server'
Stingy - Today at 6:25 PM
import discord
from typing import List

from discord.ext import commands


class MassDM:

    """Send a direct message to all members of the specified Role."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def _member_has_role(self, member: discord.Member, role: discord.Role):
        return role in member.roles

    def _get_users_with_role(self, server: discord.guild,
                             role: discord.Role) -> List[discord.User]:
        roled = []
        for member in guild.members:
            if self._member_has_role(member, role):
                roled.append(member)
        return roled

    @commands.command(no_pm=True, name="massdm",
                      aliases=["mdm"])
    async def _mdm(self, ctx: commands.Context,
                   role: discord.Role, *, message: str):
        """Sends a DM to all Members with the given Role.
        Allows for the following customizations:
        {0} is the member being messaged.
        {1} is the role they are being message through.
        {2} is the person sending the message.
        """

        server = ctx.message.guild
        sender = ctx.message.author

        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass

        dm_these = self._get_users_with_role(server, role)

        for user in dm_these:
            try:
                await self.bot.send_message(user,
                                            message.format(user, role, sender))
            except (discord.Forbidden, discord.HTTPException):
                continue


def setup(bot: commands.Bot):
    bot.add_cog(MassDM(bot))
