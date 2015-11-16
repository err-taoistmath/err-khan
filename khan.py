import re
from errbot import BotPlugin, re_botcmd

class Khan(BotPlugin):

    @re_botcmd(pattern=r"(^| )khan?( |$)", prefixed=False, flags=re.IGNORECASE)
    def khan(self, msg, match):
        return "http://24.media.tumblr.com/tumblr_lty7zyQVAL1r0gftro1_500.gif"