# -*- coding: utf-8 -*-
"""mods.py: Modules for the IRC bot.

Contains all built in commands and listeners.

"""

import sys
import time
import traceback
from const import *

# Symbian S60 specific compatibility
s60 = False
if sys.platform == "symbian_s60":
    s60 = True
    sys.path.append("e:\\python")
    sys.path.append("c:\\python")
    sys.path.append("c:\\DATA\\python")

from helpers import *
from const import *

class Args:
    def __init__(self, args=[], bot=None):
        self.bot = bot
        arg_list = []
        if type(args) != type([]):
            if args != None:
                arg_list = args.strip().split(" ")
        self.original = list(arg_list)
        self.args = list(arg_list)

    def __getitem__(self, item):
        return self.original[item]

    def __setitem__(self, item, value):
        self.original[item] = value

    def __len__(self):
        return len(self.original)

    def FirstArg(self):
        if len(self.original) != 0:
            return self.original[0]
        return ""

    def Empty(self):
        if len(self.args) == 0:
            return True
        return False

    def Range(self, start, end=None):
        if end == None:
            end = len(self.original)
        return (" ".join(self.original[start:end]))

    def Drop(self, what=0):              # drops a selected arg from list
        if type(what) == type(1):
            self.args.pop(what)
        else:
            self.args.pop(self.args.index(what))

    def IsStrSearch(sef, s):
        if s[0] != "?":return False
        return True

    def IsChannel(self, s):
        return s[0] in ["#", "&", "!"]

    def IsNick(self, s):
        return s[0] == "~"

    def IsNAccount(self, name):
        return name in self.bot.config["accounts"].keys()

    def HasType(self, what):             # checks if a type is found in args
        return self.FindType(what)

    def Take(self, what):                # returns type matched
        return self.FindType(what, True)

    def FindType(self, what, commit=False):
        for arg in self.args:
            if what == "duration":
                val = str_to_seconds(arg)
                if val != False:
                    if commit:
                        self.Drop(arg)
                        return val
                    else:return True
            elif what == "channel":
                if self.IsChannel(arg):
                    if commit:
                        self.Drop(arg)
                        return arg
                    else:return True
            elif what == "search":
                if self.IsStrSearch(arg):
                    if commit:
                        self.Drop(arg)
                        return arg[1:]
                    else:return True
            elif what == "nick":
                if self.IsNick(arg):
                    if commit:
                        self.Drop(arg)
                        return arg[1:]
                    else:return True
            elif what == "account":
                if self.IsNAccount(arg):
                    if commit:
                        self.Drop(arg)
                        return arg
                    else:return True
        return False


# Baseclas for all modules
class Module:
    def __init__(self, bot):
        self.bot = bot
        self.debug = 1

    def init(self):
        pass
        

# Baseclass for commands
class Command(Module):
    def __init__(self, bot, properties):
        Module.__init__(self,bot)
        
        self.name = properties["name"]
        self.level = properties["level"]
        self.zone = properties["zone"]
        
        self.args = Args()
        self.throttle_time = properties["throttle"]
        if self.throttle_time == None: self.throttle_time = self.bot.config["cmd_throttle"]

        self.initialized = 0
        self.users = {} # list of users of command
        
    def DebugCmd(self, *args):
        args = map(arg_to_str,args)
        line = " ".join(args)
        if self.debug:
            self.bot.BotLog("CMD: ["+self.name+"]",line )
        
    def ArgList(self, data):
        if data == None: return []
        data = data.strip()
        argobj = Args(data.split(" "))
        return argobj

    def GetMan(self):
        docstr = "-no description-"
        if "__doc__" in dir(self):
            docstr = " ".join(map(lambda s: s.strip(), self.__doc__.split("\n")))
        alias_str = ""
        aliases = self.bot.config.GetAliases(self.name)
        if aliases:
            alias_str = " (" + ", ".join(aliases) + ")"
        man = self.name + alias_str + " [" + str(self.level) + "]: " + docstr
        return man
    
    def IsAllowedWin(self, win):
        if self.zone == IRC_ZONE_BOTH:
            return True
        else:
            if win.zone != self.zone:
                return False
        return True
        
    def IsAllowedUser(self, user):
        if user.GetPermission()<self.level:
            return False
        return True

    # Determine wether the command can be run
    # Blocks command spamming
    def IsThrottled(self,user):
        if user.GetPermission() >= 5:
            return False
        else:
            if user in self.users.keys():
                t = self.users[user][0]
                if (time.time()-t) < self.throttle_time:
                    return True
                else:
                    return False
            else:
                self.users[user] = [time.time(),False]
                return False

    def GetThrottleWaitTime(self,user):
        t = self.throttle_time - int(time.time()-self.users[user][0])
        if t < 1: t=1
        return t

    def WarnThrottle(self, user):
        if self.users[user][1] == False:
            self.users[user][1] = True
            return True
        else:
            return False

    def Execute(self, win, user, data, caller=None):
        if self.IsAllowedWin(win):
            if self.IsAllowedUser(user):
                if self.IsThrottled(user):
                    if self.WarnThrottle(user):
                        win.Privmsg("can't do that so often, wait %i sec" %self.GetThrottleWaitTime(user))
                    return False
                else:
                    self.users[user] = [time.time(),False]
                    if self.bot.config["avoid_cmd_crash"]:
                        try:
                            self.args = Args(data,self.bot)
                            self.run(win,user,data)
                        except Exception,e:
                            win.Privmsg("failed to run:"+str(e))
                            print traceback.format_exc()
                            print sys.exc_info()[0]
                    else:
                        self.run(win,user,data)
                    return True
            else:
                if user.IsAuthed():
                    win.Privmsg("sry, you can't do that")
                else:
                    win.Privmsg("sry, you need to auth")
                
        else:
            win.Privmsg("you can't do that here, use privmsg")
        return False
    
    def run(self, win, user, data, caller=None):
        pass


# Base class for listeners
class Listener(Module):
    def __init__(self, bot, properties):
        Module.__init__(self, bot)

        self.name = properties["name"]
        self.zone = properties["zone"]

        self.interval = properties["interval"]
        self.last_exec = None

        self.events = []
        self.init()

    def event(self, event):
        pass

