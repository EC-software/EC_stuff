"""
    A simple IRC channel viewer.
    ver. 1.0.0 build 2014-12-13 17:00 - First working version
"""

# ToDo
#    - respond to PING, to stay alive...

import sys
import socket
import datetime

# Setup parameters
host_name = "irc.freenode.net"
num_port  = 6667
nick_name = "chvi"
user_name = "ChVi"
real_name = "Channel Viewer"
channel = "##atalk"

# Check for command line parameters, if none given just go with default values ...
print "sys.argv: ", str(type(sys.argv)), str(len(sys.argv))
print "        : ", str(sys.argv)
if len(sys.argv) != 1:
    if len(sys.argv) == 2:
        host_name = sys.argv[1].split()[0]
        channel = sys.argv[1].split()[1]
    else:
        print "Usage: IRC_chnl_view.py [\"<server_name> <channel>\"]"
        print "       Notice the \" are important as channel names often contain # ..."
        sys.exit(1)

# Print header
print "====== IRC_chnl_view.py ========================================================"
print "    Channel view for IRC"
print "    This program will echo to stdout, all messages on the specified IRC channel."
print "        Server(port): %s (%s)" % (host_name, str(num_port))
print "        Channel: %s " % channel
print "        as NICK, USER, Real name: %s, %s, %s" % (nick_name, user_name, real_name)
print "    Each raw IRC message line is preceded by a viewer time stamp [hh:mm:ss]"
print "    Send 'atalk-kickview' from another IRC client to kick the viewer."
print "================================================================================"

# Login to IRC channel
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host_name, num_port))
print "# Connected to: " +str(s.getpeername())+ " from " + str(s.getsockname())
s.send("NICK %s\r\n" % nick_name)
s.send("USER %s %s %s :%s\r\n" % (user_name, host_name, "some_server_name", real_name))
bol_wait = True # wait for MODE reply before any further commands are send
while bol_wait:
    str_recv = s.recv(4096)
    if nick_name+" MODE "+nick_name in str_recv:
        bol_wait = False
print "# Logged in ..."
s.send("JOIN %s\r\n" % channel)
#s.send("PRIVMSG "+channel+" :Channel viewer is present. Type atalk-kickview to kick it.\r\n")

# Start printing everything I see
bol_go = True
while bol_go:
    str_recv = s.recv(4096)
    timestamp = "["+datetime.datetime.now().strftime("%H:%M:%S")+"] "
    print timestamp+str_recv.strip() # This is the actual line that shows the action...

    # Look for kick messages
    if "atalk-kickview" in str_recv.lower():
        s.send("PRIVMSG "+channel+" :I received instruction to leave...\r\n")
        print "# Closing down (%s)" % str_recv.strip()
        bol_go = False
        
    # Look for "ERROR :Closing Link"
    if "error :closing link" in str_recv.lower():
        print "# Closing down (%s)" % str_recv.strip()
        bol_go = False

# Leave in peace ...
s.send("PART ##atalk\r\n")
s.send("QUIT : bol_go became False\r\n")
print "# Logged out ..."
