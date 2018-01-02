import discord

from discord.ext import commands


class MassDM:

    """Send a direct message to all members of the specified Role."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.roled=[]

    def _member_has_role(self, member: discord.Member, role: discord.Role):
        return role in member.roles

    def _get_users_with_role(self, server: discord.guild,
                             role: discord.Role):
        for member in guild.members:
            if self._member_has_role(member, role):
                self.roled.append(member)
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
            await ctx.message.delete()
        except:
            pass

        dm_these = self._get_users_with_role(server, role)

        for user in dm_these:
            try:
               user.send("Your message goes here")
            except (discord.Forbidden, discord.HTTPException):
                continue


def setup(bot: commands.Bot):
    bot.add_cog(MassDM(bot))
