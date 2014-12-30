""" A simple IRC bot, to exercise before implementing IRC into A-talk
   (https://github.com/MartinHvidberg/Atalk/wiki/1.-A%E2%80%93talk.-The-main-page)"""

import sys
import socket
import string

host_name = "irc.freenode.net"
num_port  = 6667
nick_name = "atlk" # My bot name
user_name = "Atlk"
real_name = "Atalk bot"
pass_word = "atalk" # pw = atalk
channel = "##atalk"

def msg(msg):
    s.send("PRIVMSG "+channel+" :"+msg+"\r\n")
    return 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host_name, num_port))
print "Connected to: " +str(s.getpeername())+ " from " + str(s.getsockname())
s.send("PASS %s\r\n" % pass_word)
s.send("NICK %s\r\n" % nick_name)
s.send("USER %s %s %s :%s\r\n" % (user_name, host_name, "some_server_name", real_name))
bol_wait = True # wait for MODE reply before any further commands are send
while bol_wait:
    str_recv = s.recv(4096)
    if nick_name+" MODE "+nick_name in str_recv:
        bol_wait = False
print "Logged in ..."
s.send("JOIN %s\r\n" % channel)
#s.send("LIST %s\r\n" % "##")
msg("The Atalk-bot is up. Write 'atalk-cmds' to see the commands...")

bol_go = True
#time.sleep(10)
while bol_go:
    str_recv = s.recv(4096)
    
    if ("atalk-ping" in str_recv.lower()):
        num_pos = str_recv.find("atalk-ping") 
        msg("atalk-pong "+str_recv[num_pos+11:]) # plus length of command
   
    if ("atalk-salm" in str_recv.lower()):
        a_long_message = "1...................................................................................................100.................................................................................................200.................................................................................................300.................................................................................................400.................................................................................................500........x"
        msg(a_long_message)
   
    if "atalk-kickbot" in str_recv.lower():
        msg("I received instruction to leave...")
        print "Closing down (%s)" % str_recv.strip()
        bol_go = False
    
    if ("atalk-cmds" in str_recv.lower()):
        msg("Atalk Bot Commands = atalk-cmds, -ping, -salm, -kickbot")

s.send("PART ##atalk\r\n")

bol_wait = False
while bol_wait:
    str_recv = s.recv(4096)
    if len(str_recv) > 0:
        print str_recv
    else:
        bol_wait = False
        
s.send("QUIT : bol_go became False\r\n")
print "QUIT"
